import psycopg2
from clcrypto import hash_password
from db_connection import connect


class User:
    db_name = 'test1'

    def __init__(self, username="", password="", salt=None):
        self._id = None
        self.username = username
        self._hashed_password = hash_password(password, salt)

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password, salt=None):
        self._hashed_password = hash_password(password, salt)

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)

    def save_to_db(self):
        conn = connect(User.db_name)
        cursor = conn.cursor()
        if self._id is None:
            sql = f"""
            INSERT INTO users(username, hashed_password) VALUES ('{self.username}', '{self.hashed_password}')
            """
            cursor.execute(sql)
        else:
            sql = f"""
            UPDATE users SET username='{self.username}', hashed_password='{self.hashed_password}' WHERE id={self.id}
            """
            cursor.execute(sql)
        conn.close()
        return True

    @staticmethod
    def load_user_by_username(username):
        conn = connect(User.db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT (id, username, hashed_password) FROM users WHERE username='{username}'
        """
        cursor.execute(sql)
        data = cursor.fetchone()
        if data:
            data = data[0][1:-1].split(sep=",")
            loaded_user = User(username)
            loaded_user._id = data[0]
            loaded_user._hashed_password = data[2]
            return loaded_user

    @staticmethod
    def load_user_by_id(id):
        conn = connect(User.db_name)
        cursor = conn.cursor()
        sql = f"""
            SELECT (id, username, hashed_password) FROM users WHERE id='{id}'
            """
        cursor.execute(sql)
        data = cursor.fetchone()
        if data:
            data = data[0][1:-1].split(sep=",")
            loaded_user = User(data[1])
            loaded_user._id = data[0]
            loaded_user._hashed_password = data[2]
            return loaded_user

    @staticmethod
    def load_all_users():
        conn = connect(User.db_name)
        cursor = conn.cursor()
        sql = f"""
                    SELECT id, username, hashed_password FROM users
                    """
        cursor.execute(sql)
        data = cursor.fetchall()
        loaded_users = []
        if data:
            for elem in data:
                loaded_user = User(elem[1])
                loaded_user._id = elem[0]
                loaded_user._hashed_password = elem[2]
                loaded_users.append(loaded_user)
        return loaded_users

    def delete(self):
        conn = connect(User.db_name)
        cursor = conn.cursor()
        sql = f"DELETE FROM users WHERE id={self._id}"
        cursor.execute(sql)
        self._id = None
        return True

class Messages:
    db_name = 'test1'

    def __init__(self, from_id, to_id, text):
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self._id = None
        self.creation_data = None

    @property
    def id(self):
        return self._id

    def save_to_db(self):
        conn = connect(User.db_name)
        cursor = conn.cursor()
        if self._id is None:
            sql = f"""
            INSERT INTO messages (from_id, to_id, text) VALUES ('{self.from_id}', '{self.to_id}','{self.text}')
            """
            cursor.execute(sql)
        else:
            sql = f"""
            UPDATE messages SET from_id='{self.from_id}', to_id='{self.to_id}', text='{self.text}' WHERE id={self.id}
            """
            cursor.execute(sql)
        conn.close()
        return True

    @staticmethod
    def load_all_messages():
        conn = connect(User.db_name)
        cursor = conn.cursor()
        sql = f"""
                        SELECT * FROM messages
                        """
        cursor.execute(sql)
        data = cursor.fetchall()
        loaded_messages = []
        if data:
            for elem in data:
                loaded_message = Messages(elem[1],elem[2],elem[3])
                loaded_message._id = elem[0]
                loaded_message.creation_data = elem[4]
                loaded_messages.append(loaded_message)
        return loaded_messages


if __name__ == '__main__':
    pass