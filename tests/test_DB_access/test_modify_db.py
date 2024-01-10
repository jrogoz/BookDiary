import unittest
import psycopg2
from DB_access.modify_db import exec_query


class TestModifyDB(unittest.TestCase):
    def test_exec_query_OK_not_select(self):
        query = "UPDATE books set author = 'inny' where book_id = 3"
        result = exec_query(query)
        self.assertEqual(None, result)

    def test_exec_query_OK_select(self):
        query = "SELECT * FROM books"
        result = exec_query(query)
        self.assertNotEqual(None, result)

    def test_exec_query_not_string(self):
        query = "5"
        exec_query(query)
        self.assertRaises(psycopg2.DatabaseError)

