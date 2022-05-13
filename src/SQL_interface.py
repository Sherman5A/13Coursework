# SQLite provides a lightweight disk-based database
import sqlite3
# Error catcher for try except.
from sqlite3.dbapi2 import Cursor, Error


class sqlInterface:
    """Class that is made to interact with a SQLite file database."""

    def __init__(self, file):
        """Initialise the sqlInterface, argument defines 
        the database file which is connected to / made."""
        self.file = file
    
    def create_connection(self):
        """Create a connection to the database."""
        self.connection = None
        # Try to make a connection to the database
        try:
            self.connection = sqlite3.connect(self.file)
            self.cursor = self.connection.cursor()
        # If an error occurs, print it.
        except Error as e:
            print(e)
      
    def create_table(self, sql_command):
        """Create a table in the sql database."""
        # Try to execute the sql_command given in the arguments.
        try:
            self.cursor.execute(sql_command)
        except Error as e:
            print(e)
    
    def get_data(self, sql_command, values=None):
        """Get data from the database."""
        # Performing operator overloading, this allows for polymorphism
        # Allows user to put the SQL command"s values in either the command 
        # string or as a separate argument.
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
                # Commit the changes to the database
                self.connection.commit()
            except Error as e:
                print(e)
        else:  # Values argument is not left blank.
            try:
                self.cursor.execute(sql_command, values)
                # Commit the changes to the database
                self.connection.commit()
            except Error as e:
                print(e)
