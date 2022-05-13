# Datetime is used to check if dates exist and are formatted correctly.
from datetime import datetime
# Validation is used to validate strings, integers, passwords, etc.
import validation
# SQL_interface is used to write and access the database.
import SQL_interface


def create_user(account_variables):
    """"Create a new user, performs validation, then adds to sql table"""

    # Creating class interfaces, passing in DB to connect to.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Create connection to the database defined above ^
    sql_database.create_connection()

    def create_table():
        """Creates user table"""

        # SQL command to create table if it does not exist.
        sql_create_user_table = """ CREATE TABLE IF NOT EXISTS users (
                                "id" INTEGER,
                                access_level TEXT NOT NULL,
                                first_name TEXT NOT NULL,
                                second_name TEXT NOT NULL,
                                year_group TEXT NOT NULL,
                                form_group TEXT NOT NULL,
                                username TEXT NOT NULL,
                                password TEXT NOT NULL,
                                PRIMARY KEY("id" AUTOINCREMENT)
                            ); """
        sql_database.create_table(sql_create_user_table)

    def write_user():
        """Write variable to database table"""

        # Inserts data into table.
        sql_database.insert_data(
            "INSERT INTO users(first_name, access_level, second_name, "
            "year_group, form_group, username, password) VALUES(?, ?, ?, ?, "
            "?, ?, ?);",
            (account_variables['first_name'],
             account_variables['access_level'],
             account_variables['second_name'],
             account_variables['year_group'],
             account_variables['form_group'],
             account_variables['username'],
             account_variables['password']))

        
    # Validation processes. Iterates through the user's inputs. 
    # If validation is incorrect, a False boolean and a
    # reason is returned.
    for key, value in account_variables.items():

        # If value is empty or above 20 characters, return False.
        if not validation.len_check(value, 20):
            return False, key, 'Length check, check that field is not empty and is ' \
                               'under 20 characters '

        # Names require string checks as no symbols should be accepted.
        if key == 'first_name' or key == 'second_name':
            if not validation.string_check(value):
                return False, key, 'Alpha check'

    # Check if the password and repeated password the user entered match.           
    if account_variables['password'] != account_variables['password_repeat']:
        return False, 'password', "Passwords don't match"

    # Check if password is strong enough.
    if not validation.password_strength(account_variables['password']):
        return False, 'password', 'Password not strong enough. Use >= 7 ' \
                                  'characters and both upper and lower case ' \
                                  'letters'

    # Create table before common username query to avoid errors if the database
    # is new and the user table does not exist.
    create_table()

    # Check for duplicate usernames. Usernames must be unique as they are
    # used for log in. If there are 2 same usernames, which password is the
    # correct one?
    common_usernames = sql_database.get_data(
        "SELECT username FROM users WHERE username=?",
        (account_variables['username'],))
    if len(common_usernames) != 0:
        return False, 'username', 'Username is not unique'

    # After all validation has passed, write the information to the database 
    # table.
    write_user()
    
    # Returns True boolean to let the GUI class that everything was successful.
    return True  


def login(input_username, input_password):
    """Login to SQL"""
    
    # Creating class interfaces, passing in DB to connect to.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Create connection to the database defined above ^
    sql_database.create_connection()
    # Get all occurrences of the user's login inputs. 
    sql_search_login_details = sql_database.get_data(
        """SELECT id, access_level, first_name, second_name, year_group, 
        form_group, username, password FROM users WHERE username=? AND password=?""",
        (input_username, input_password))
    # If the password and username match, then return true.
    try:
        if len(sql_search_login_details) == 1:
            return True, sql_search_login_details
    # If there are no occurrences, return false
    except TypeError:   
        return False


def create_sign_in(student_id):
    """Create sign in in database using student_id"""

    # Creating class interfaces, passing in db to connect to.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Create connection to database above.
    sql_database.create_connection()

    # SQL command to create a sign in table. Avoids error if the table does not
    # exist.
    sql_create_table = """CREATE TABLE IF NOT EXISTS sign_in (
    "sign_in_id" INTEGER,
    "date" TEXT NOT NULL,
    "time" TEXT NOT NULL,
    "student_id" INTEGER NOT NULL,
    FOREIGN KEY("student_id") REFERENCES "users"("id") ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY("sign_in_id" AUTOINCREMENT)
    );"""

    sql_database.create_table(sql_create_table)
    # Insert the data into the table. Dates and times are generated
    # automatically. The student ID is manually passed as an argument.
    sql_database.insert_data("INSERT INTO sign_in(date, time, student_id) "
                             "VALUES(date('now'), time('now'), ?)", student_id)


def create_sign_out(student_id, sign_out_type):
    """"Create sign out in database using args: student_id and sign_out_type"""

    # Creating class interfaces, passing in db to connect to.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Create connection to database.
    sql_database.create_connection()

    # SQL command to create a sign out table. Avoids error if the table does not
    # exist.
    sql_create_table = """CREATE TABLE IF NOT EXISTS sign_out (
        "sign_out_id" INTEGER,
        "date" TEXT NOT NULL,
        "time" TEXT NOT NULL,
        "student_id" INTEGER NOT NULL,
        "sign_out_type" TEXT NOT NULL,
        FOREIGN KEY("student_id") REFERENCES "users"("id") ON UPDATE CASCADE ON DELETE CASCADE,
        PRIMARY KEY("sign_out_id" AUTOINCREMENT)
        );"""
    # Execute the create table command
    sql_database.create_table(sql_create_table)
    
    # Insert the sign out data into the created table.
    sql_database.insert_data(
        "INSERT INTO sign_out(date, time, student_id, sign_out_type) VALUES("
        "date('now'), time('now'), ?, ?)",
        (student_id, sign_out_type))


def search_signs(sign_in_or_out, search_terms, time_tuple=None):
    """Searches the sign tables with the args provided."""

    # Depending on the argument 'sign_in_or_out' either search the sign out
    # or sign in the database table.
    if sign_in_or_out == 'sign out':
        sql_search = "SELECT * FROM sign_out"
    elif sign_in_or_out == 'sign in':
        sql_search = "SELECT * FROM sign_in"

    # If there are items in search_terms or time_tuple, add them to the search.
    if len(search_terms) != 0 or time_tuple is not None:
        sql_search += " WHERE "
        # If there are items in time_tuple, add them to the search.
        if time_tuple is not None:
            sql_search += "time BETWEEN '{}' AND '{}'".format(time_tuple[0],
                                                              time_tuple[1])
            if len(search_terms) != 0:
                sql_search += ' AND '
        # If there are items in search_terms, add them to the search.
        if len(search_terms) != 0:
            sql_search += ' AND '.join(
                '='.join((key, "'{}'".format(value))) for key, value in
                search_terms.items())
        # Add ; to end the search after all search values are 
        # added to terminate search
        sql_search += ';'

    # Create SQL connection.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Connect to the database
    sql_database.create_connection()
    # Execute and return SQL search result.
    return sql_database.get_data(sql_search)


def sign_history():

    # List to store all of the sign ins.
    all_signs = []
    # Add all sign outs to the list.
    all_signs.extend(search_signs('sign out', {}))
    # Add all sign ins to the list.
    all_signs.extend(search_signs('sign in', {}))
    # Performing a sort on the taken sign in and signs outs. It sorts by most recent to oldest.
    return sorted(all_signs, key=lambda x: datetime.strptime('{} {}'.format(x[1], x[2]), '%Y-%m-%d %H:%M:%S'), reverse=True)


def search_users(search_terms):
    """Searches the user tables with the dictionary provided in args."""

    # If no terms are provided, return all users.
    if len(search_terms) != 0:
        sql_search = "SELECT * FROM users WHERE "
        # Takes keys, values, formats value, joins them with '=', and then
        # adds 'AND' between dict keys. Finally, adds ';' to end the SQL statement.
        sql_search += ' AND '.join(
            '='.join((key, "'{}'".format(value))) for key, value in
            search_terms.items()) + ';'
    else:
        sql_search = "SELECT * FROM users;"

    # Create a database interface class
    sql_database = SQL_interface.sqlInterface('test.db')
    # Connect to the database using the interface class
    sql_database.create_connection()
    # Execute and return sql search result.
    return sql_database.get_data(sql_search)


def edit_user(user_id, edited_terms):

    # Create the start of an SQL statement that updates the information of the 
    # student given by user_id, with the terms provided in edited_terms.
    sql_statement = """UPDATE users """ \
                    """SET """
    # Get the edited terms and add them to the SQL command with the correct
    # formatting
    sql_statement += ', '.join('='.join((key, "'{}'".format(value))) for key, value in
                                  edited_terms.items()) + ' WHERE id = {};'.format(user_id)
    sql_database = SQL_interface.sqlInterface('test.db')
    # Connect to the database using the interface class
    sql_database.create_connection()
    # Execute the sql_statement created. This updates the user with the ID
    # given in the argument.
    sql_database.insert_data(sql_statement)


def delete_user(user_id):

    # Create SQL statement to execute.
    sql_statement = """DELETE FROM users WHERE id = {};""".format(user_id)
    # Create a database interface class.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Connect to the database using the interface class.
    sql_database.create_connection()
    # Execute the sql_statement created. This deletes the user with the ID
    # given in the argument.
    sql_database.insert_data(sql_statement)


def edit_sign_in(sign_in_id, edited_terms):
    
    # Create the start of an SQL statement that updates the information of the 
    # sign in given by sign_in_id, with the terms provided in edited_terms.
    sql_statement = 'UPDATE sign_in SET '
    # Format the edited terms into an SQL command
    sql_statement += ', '.join('='.join((key, "'{}'".format(value))) 
                               for key, value in edited_terms.items()) + ' WHERE sign_in_id = {};'.format(sign_in_id)
    # Create a class that interfaces with the SQL database.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Connect to the SQL database.
    sql_database.create_connection()
    # Execute the command, updating the sign in.
    sql_database.insert_data(sql_statement)


def delete_sign_in(sign_in_id):

    # Delete the sign in with the id, sign_in_id.
    sql_statement = 'DELETE FROM sign_in WHERE sign_in_id = {}'.format(sign_in_id)
    # Create a class that interfaces with the SQL database.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Connect to the SQL database.
    sql_database.create_connection()
    # Execute the command, deleting the sign in.
    sql_database.insert_data(sql_statement)


def edit_sign_out(sign_out_id, edited_terms):

    # SQL command that edits the sign out with the ID given in the arguments.
    sql_statement = 'UPDATE sign_out SET '
    # Formatting the SQL statement correctly.
    sql_statement += ', '.join('='.join((key, "'{}'".format(value))) 
                               for key, value in edited_terms.items()) + ' WHERE sign_out_id = {};'.format(sign_out_id)
    # Create a class that interfaces with the SQL database.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Connect to the SQL database.
    sql_database.create_connection()
    # Execute the command, deleting the sign in.
    sql_database.insert_data(sql_statement)


def delete_sign_out(sign_out_id):
    
    # Delete selected sign out.
    sql_statement = 'DELETE FROM sign_out WHERE sign_out_id = {}'.format(sign_out_id)
    # Create a class that interfaces with the SQL database.
    sql_database = SQL_interface.sqlInterface('test.db')
    # Connect to the SQL database.
    sql_database.create_connection()
    # Execute the command, deleting the sign in.
    sql_database.insert_data(sql_statement)
