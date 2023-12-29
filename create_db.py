from DB_access.connection import connect, disconnect


def create_books_table(connection, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id serial PRIMARY KEY,
            title VARCHAR(75) NOT NULL,
            author VARCHAR(50) NOT NULL
        );
    """
    )
    connection.commit()


def create_status_table(connection, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS status (
            status_id serial PRIMARY KEY,
            status_name VARCHAR(25) NOT NULL
        );
    """
    )
    connection.commit()


def create_book_status_table(connection, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_status (
            book_id INT NOT NULL,
            status_id INT NOT NULL,
            start_date TIMESTAMP,
            end_date TIMESTAMP,
            PRIMARY KEY (book_id, status_id),
            FOREIGN KEY (book_id)
                REFERENCES books (book_id),
            FOREIGN KEY (status_id)
                REFERENCES status (status_id)
        );
    """
    )
    connection.commit()


def create_db(connection, cursor):
    create_books_table(cursor)
    create_status_table(cursor)
    create_book_status_table(connection, cursor)


if __name__ == "__main__":
    conn, cur = connect()
    create_db(conn, cur)
    disconnect(conn, cur)

