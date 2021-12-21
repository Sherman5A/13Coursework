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
      
    def create_table(self, sql_command):       
        try:
            self.cursor.execute(sql_command)
        except Error as e:
            print(e)

    
    def get_data(self, sql_command, values=None):
        if values == None:
            try:
                self.cursor.execute(sql_command)
                return self.cursor.fetchall()
            except Error as e:
                print(e)
        else:
            try:
                self.cursor.execute(sql_command, values)
                return self.cursor.fetchall()
            except Error as e:
                print(e)

    def insert_data(self, sql_command, values):
        
        try:
            self.cursor.execute(sql_command, values)
            self.connection.commit()
        except Error as e:
            print(e)
            
