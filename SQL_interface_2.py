import sqlite3
from sqlite3.dbapi2 import Cursor, Error


class SQL_inter():

    def __init__(self, file):
        self.file = file
    
    def create_connection(self):
        self.connection = None
        try:
            self.connection = sqlite3.connect(self.file)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(e)
      
    def execute_sql(self, sql_command):
        try:
            self.cursor.execute(sql_command)
        except Error as e:
            print(e)
