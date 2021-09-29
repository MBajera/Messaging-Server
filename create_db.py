import psycopg2
from db_connection import connect


def db_creation(db_name):
    conn = connect()
    cursor = conn.cursor()
    sql = f"CREATE DATABASE {db_name}"
    try:
        cursor.execute(sql)
        conn.close()
    except psycopg2.errors.DuplicateDatabase:
        return False
    return True


def db_tables_creation(db_name):
    conn = connect(db_name)
    cursor = conn.cursor()
    sql = """
    CREATE TABLE users(
    id serial,
    username varchar(255) unique,
    hashed_password varchar(80),
    PRIMARY KEY (id)
    );
    CREATE TABLE messages(    id serial,
    from_id integer,
    to_id integer,
    text varchar(255),
    creation_date timestamp default current_timestamp,
    PRIMARY KEY (id),
    foreign key (from_id) REFERENCES users(id),
    foreign key (to_id) REFERENCES users(id));
    """
    cursor.execute(sql)
    conn.close()


if __name__ == '__main__':
     a = db_tables_creation('test1')
