import unittest
import psycopg2
from DB_access.modify_db import exec_query, create_new_table, insert_into_table, delete_from_table
from DB_access.connection import connect, disconnect
from config import config


class TestExecQuery(unittest.TestCase):
    def setUp(self):
        self.conn, self.cur = connect()
        self.table_name = 'test_books'
        self.create_test_table()

    def tearDown(self):
        delete_from_table(self.table_name)
        disconnect(self.conn, self.cur)

    def create_test_table(self):
        table_cols = {
            "book_id": "serial PRIMARY KEY",
            "title": "VARCHAR(75) NOT NULL",
            "author": "VARCHAR(50) NOT NULL"
        }
        create_new_table(self.table_name, **table_cols)

        book_1 = {'title': 'book_title_1',
                  'author': 'book_author_1'}
        book_2 = {'title': 'book_title_2',
                  'author': 'book_author_2'}
        book_3 = {'title': 'book_title_3',
                  'author': 'book_author_3'}
        book_4 = {'title': 'book_title_4',
                  'author': 'book_author_4'}

        insert_into_table(self.table_name, **book_1)
        insert_into_table(self.table_name, **book_2)
        insert_into_table(self.table_name, **book_3)
        insert_into_table(self.table_name, **book_4)

    def test_exec_query_OK_not_select(self):
        query = f"UPDATE {self.table_name} set author = 'inny' where book_id = 3"
        result = exec_query(query)
        self.assertEqual(None, result)

    def test_exec_query_OK_select(self):
        query = f"SELECT * FROM {self.table_name}"
        result = exec_query(query)
        self.assertNotEqual(None, result)


class TestCreateNewTable():
    pass


class TestInsertIntoTable():
    pass