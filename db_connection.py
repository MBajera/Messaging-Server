import psycopg2


def connect(db_name=None):
    if db_name == None:
        connection_data = {'user': 'postgres', 'password': 'coderslab','port': 5432,'host': 'localhost'}
    else:
        connection_data = {'user': 'postgres', 'password': 'coderslab','port': 5432,'host': 'localhost','dbname':db_name}

    connection = psycopg2.connect(**connection_data)
    connection.autocommit = True

    return connection


if __name__ == '__main__':
    connection = connect()
    connection.close()
