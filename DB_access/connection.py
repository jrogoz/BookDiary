import psycopg2
from config import config


def connect():
    connection = None
    cursor = None

    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        #print('PostgreSQL database version: ')
        #cursor.execute('SELECT version()')
        #db_version = cursor.fetchone()
        #print(db_version)

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
            # print('Database connection terminated.')