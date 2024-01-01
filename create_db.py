from DB_access.connection import connect, disconnect
from DB_access.modify_db import create_new_table, insert_into_table
from DB_access.select import select_from_table


def create_books_table():

    col_dict = {
        "book_id": "serial PRIMARY KEY",
        "title": "VARCHAR(75) NOT NULL",
        "author": "VARCHAR(50) NOT NULL"
    }
    create_new_table("books", **col_dict)


def create_status_table():

    col_dict = {
        "status_id": "serial PRIMARY KEY",
        "status_name": "VARCHAR(25) NOT NULL"
    }
    create_new_table( "status", **col_dict)


def create_book_status_table():

    col_dict = {
        "book_id": "INT NOT NULL",
        "status_id": "INT NOT NULL",
        "start_date": "TIMESTAMP",
        "end_date": "TIMESTAMP",
        "PRIMARY KEY": "(book_id, status_id)",
        "FOREIGN KEY (book_id)": "REFERENCES books (book_id)",
        "FOREIGN KEY (status_id)": "REFERENCES status (status_id)"
    }
    create_new_table("book_status", **col_dict)


def create_db():
    create_books_table()
    create_status_table()
    create_book_status_table()


if __name__ == "__main__":
    create_db()
    select_from_table("books", 1)
