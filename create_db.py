from DB_access.connection import connect, disconnect
from DB_access.modify_db import create_new_table, insert_into_table


def create_books_table(connection, cursor):

    col_dict = {
        "book_id": "serial PRIMARY KEY",
        "title": "VARCHAR(75) NOT NULL",
        "author": "VARCHAR(50) NOT NULL"
    }
    create_new_table(connection, cursor, "books", **col_dict)


def create_status_table(connection, cursor):

    col_dict = {
        "status_id": "serial PRIMARY KEY",
        "status_name": "VARCHAR(25) NOT NULL"
    }
    create_new_table(connection, cursor, "status", **col_dict)


def create_book_status_table(connection, cursor):

    col_dict = {
        "book_id": "INT NOT NULL",
        "status_id": "INT NOT NULL",
        "start_date": "TIMESTAMP",
        "end_date": "TIMESTAMP",
        "PRIMARY KEY": "(book_id, status_id)",
        "FOREIGN KEY (book_id)": "REFERENCES books (book_id)",
        "FOREIGN KEY (status_id)": "REFERENCES status (status_id)"
    }
    create_new_table(connection, cursor, "book_status", **col_dict)


def create_db(connection, cursor):
    create_books_table(connection, cursor)
    create_status_table(connection, cursor)
    create_book_status_table(connection, cursor)


if __name__ == "__main__":
    conn, cur = connect()
    create_db(conn, cur)

    dict_col = {
        "title": "'Harry_Potter_i_Komnata_Tajemnic'",
        "author": "'J.K. Rowling'"
    }

    insert_into_table(conn, cur, "books", **dict_col)
    disconnect(conn, cur)

