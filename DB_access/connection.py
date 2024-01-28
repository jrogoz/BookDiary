import psycopg2
from config import config


def connect(filename='database.ini'):
    connection = None
    cursor = None

    try:
        params = config(filename)
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return connection, cursor


def disconnect(connection, cursor):

    try:
        if cursor is not None:
            cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()