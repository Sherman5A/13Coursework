from os import error
from SQLInterface import create_connection
import sqlite3
from sqlite3.dbapi2 import Cursor, Error


class SQL_inter():

    def __init__(self, file):
        self.file = file
    
    def create_connection(self):
        self.connection = None
        try:
            self.connection = sqlite3.connect(self.file)
        except Error as e:
            print(e)
        return not self.connection == None
        
    
    def create_table(self, sql_command):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_command)
        except Error as e:
            print(e)
