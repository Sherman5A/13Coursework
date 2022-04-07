import sqlite3
from sqlite3.dbapi2 import Cursor, Error


class sqlInterface:
    """Class that is made to interact with a SQLite file database."""

    def __init__(self, file):
        """Intialise the sqlInterface, argument defines 
        the database file which is connected to / made."""
        self.file = file
    
    def create_connection(self):
        """Create a connection to the database."""
        self.connection = None
        try:
            self.connection = sqlite3.connect(self.file)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(e)
      
    def create_table(self, sql_command):
        """Create a table in the sql database."""
        try:
            self.cursor.execute(sql_command)
        except Error as e:
            print(e)
    
    def get_data(self, sql_command, values=None):
        """Get data from the database."""
        # Performing operator overloading, this allows for polymorphism
        # Allows user to put the SQL command"s values in either the command 
        # string or as a seperate argument.
        if values is None:
            try:
                self.cursor.execute(sql_command)
                return self.cursor.fetchall()
            except Error as e:  # If sql database returns an error, print it
                print(e)
                return False
        else:  # Values argument is not left blank
            try:
                self.cursor.execute(sql_command, values)
                return self.cursor.fetchall()
            except Error as e:
                print(e)

    def insert_data(self, sql_command, values=None):
        """Insert data into the database."""
        # Overloading
        # Allows user to put values in string or as a seperate argument.
        if values is None:
            try:
                self.cursor.execute(sql_command)
                self.connection.commit()
            except Error as e:
                print(e)
        else:  # Values argument is not left blank.
            try:
                self.cursor.execute(sql_command, values)
                self.connection.commit()
            except Error as e:
                print(e)
