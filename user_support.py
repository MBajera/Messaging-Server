from models import User
from clcrypto import check_password


def user_support():
    while True:
        decision = int(input("""Write numer of fuction you want to choose:
        1 - Add user
        2 - Password edit
        3 - Delete user
        4 - Users list
        5 - Exit
        """))
        if decision == 5:
            break
        elif decision == 1:
            while True:
                username = input("Write username: ")
                password = input("Write password: ")
                reply = user_support_add_user(username, password)
                print(reply)
                if reply == "You did it":
                    break
        elif decision == 2:
            while True:
                username = input("Write username: ")
                password = input("Write password: ")
                new_pass = input("Write new password: ")
                reply = user_support_password_edit(username, password, new_pass)
                print(reply)
                if reply == "You did it":
                    break
        elif decision == 3:
            while True:
                username = input("Write username: ")
                password = input("Write password: ")
                reply = user_support_delete_user(username, password)
                print(reply)
                if reply == "You deleted yourself":
                    break
        elif decision == 4:
            print(user_support_users_list())


def user_support_add_user(username, password):
    users = User.load_all_users()
    for user in users:
        if user.username == username:
            return "Wrong username"
    if len(password) < 8:
        return "Too short password"
    user = User(username, password)
    user.save_to_db()
    return "You did it"


def user_support_password_edit(username, password, new_pass):
    users = User.load_all_users()
    user = None
    for elem in users:
        if elem.username == username:
            user = elem
            break
    if not user:
        return "Wrong username"
    if not check_password(password, user.hashed_password):
        return "Wrong password"
    if len(new_pass) < 8:
        return "Too short password"
    user.set_password(new_pass)
    user.save_to_db()
    return "You did it"


def user_support_delete_user(username, password):
    users = User.load_all_users()
    user = None
    for elem in users:
        if elem.username == username:
            user = elem
            break
    if not user:
        return "Wrong username"
    if not check_password(password, user.hashed_password):
        return "Wrong password"
    user.delete()
    return "You deleted yourself"


def user_support_users_list():
    users = User.load_all_users()
    list = """Users list:\n"""
    for user in users:
        list += f"User id: {user.id}, User name: {user.username}\n"
    return list


if __name__ == '__main__':
    pass
