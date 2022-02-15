from src import SQL_interface
import unittest
import os


class TestSQLInterface(unittest.TestCase):

    def setUp(self):
        self.sql_interface = SQL_interface.sqlInterface('testing.db')
        self.sql_interface.create_connection()

    def tearDown(self):
        os.remove('testing.db')

    def test_create_table(self):
        self.sql_interface.create_table("""CREATE TABLE IF NOT EXISTS test_table (
                                        "test_field" INTEGER
                                    );""")
        sql_result = self.sql_interface.get_data("""SELECT name FROM sqlite_master WHERE type='table' AND name='test_table';""")
        self.assertEqual(sql_result[0][0], 'test_table')

    def test_get_insert_data(self):
        self.sql_interface.create_table("""CREATE TABLE IF NOT EXISTS "test_table" (
	                                        "test_field"	INTEGER
                                           );""")
        self.sql_interface.insert_data("""INSERT INTO test_table(test_field) VALUES('12')""")
        check_for_new_value = self.sql_interface.get_data("""SELECT test_field FROM test_table""")
        self.assertEqual(str(check_for_new_value[0][0]), '12')
