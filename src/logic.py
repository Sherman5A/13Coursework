
from datetime import datetime
import validation
import SQL_interface


def create_user(account_variables):
    """"Create a new user, performs validation, then adds to sql table"""

    # creating class interfaces, passing in db to connect to
    sql_database = SQL_interface.sqlInterface('test.db')
    # create connection to database
    sql_database.create_connection()

    def create_table():
        """Creates user table"""

        # SQL command to create table if it does not exist
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

        # inserts data into table
        sql_database.insert_data(
            "INSERT INTO users(first_name, access_level, second_name, "
            "year_group, form_group, username, password) VALUES(?, ?, ?, ?, "
            "?, ?, ?);",
            (
                account_variables['first_name'],
                account_variables['access_level'],
                account_variables['second_name'],
                account_variables['year_group'],
                account_variables['form_group'],
                account_variables['username'],
                account_variables['password']))

    # validation
    for key, value in account_variables.items():

        # if value is empty or above 20 characters, decline
        if not validation.len_check(value, 20):
            return False, key, 'Length check, check that field is not empty and is ' \
                               'under 20 characters '

        # names require string checks as no symbols should be accepted
        if key == 'first_name' or key == 'second_name':
            if not validation.string_check(value):
                return False, key, 'Alpha check'

    # check if passwords match           
    if account_variables['password'] != account_variables['password_repeat']:
        return False, 'password', "Passwords don't match"

    # check if password is strong enough
    if not validation.password_strength(account_variables['password']):
        return False, 'password', 'Password not strong enough. Use >= 7 ' \
                                  'characters and both upper and lower case ' \
                                  'letters'

    create_table()

    # check for duplicate usernames. Usernames must be unique as they are
    # used for log in
    common_usernames = sql_database.get_data(
        "SELECT username FROM users WHERE username=?",
        (account_variables['username'],))
    if len(common_usernames) != 0:
        return False, 'username', 'Username is not unique'

    write_user()
    return True  # returns everything successful flag


def login(input_username, input_password):
    """Login to SQL"""
    
    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    sql_search_login_details = sql_database.get_data(
        """SELECT id, access_level, first_name, second_name, year_group, 
        form_group, username, password FROM users WHERE username=? AND password=?""",
        (input_username, input_password))
        
    if len(sql_search_login_details) == 1:
        return True, sql_search_login_details
    else:   
        return False


def create_sign_in(student_id):
    """Create sign in in database using student_id"""

    # creating class interfaces, passing in db to connect to
    sql_database = SQL_interface.sqlInterface('test.db')
    # create connection to database
    sql_database.create_connection()

    sql_create_table = """CREATE TABLE IF NOT EXISTS sign_in (
    "sign_in_id" INTEGER,
    "date" TEXT NOT NULL,
    "time" TEXT NOT NULL,
    "student_id" INTEGER NOT NULL,
    FOREIGN KEY("student_id") REFERENCES "users"("id") ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY("sign_in_id" AUTOINCREMENT)
    );"""

    sql_database.create_table(sql_create_table)
    sql_database.insert_data("INSERT INTO sign_in(date, time, student_id) "
                             "VALUES(date('now'), time('now'), ?)", student_id)


def create_sign_out(student_id, sign_out_type):
    """"Create sign out in database using args: student_id and sign_out_type"""

    # creating class interfaces, passing in db to connect to
    sql_database = SQL_interface.sqlInterface('test.db')
    # create connection to database
    sql_database.create_connection()

    sql_create_table = """CREATE TABLE IF NOT EXISTS sign_out (
        "sign_out_id" INTEGER,
        "date" TEXT NOT NULL,
        "time" TEXT NOT NULL,
        "student_id" INTEGER NOT NULL,
        "sign_out_type" TEXT NOT NULL,
        FOREIGN KEY("student_id") REFERENCES "users"("id") ON UPDATE CASCADE ON DELETE CASCADE,
        PRIMARY KEY("sign_out_id" AUTOINCREMENT)
        );"""
    sql_database.create_table(sql_create_table)

    sql_database.insert_data(
        "INSERT INTO sign_out(date, time, student_id, sign_out_type) VALUES("
        "date('now'), time('now'), ?, ?)",
        (student_id, sign_out_type))


def search_signs(sign_in_or_out, search_terms, time_tuple=None):
    """Searches the sign tables with the args provided."""

    # if sign_in_or_out == '' or sign_in_or_out == 'both':
    #     sql_search = "SELECT * FROM sign_in, sign_out"
    if sign_in_or_out == 'sign out':
        sql_search = "SELECT * FROM sign_out"
    elif sign_in_or_out == 'sign in':
        sql_search = "SELECT * FROM sign_in"

    if len(search_terms) != 0 or time_tuple is not None:
        sql_search += " WHERE "
        if time_tuple is not None:
            sql_search += "time BETWEEN '{}' AND '{}'".format(time_tuple[0],
                                                              time_tuple[1])
            if len(search_terms) != 0:
                sql_search += ' AND '

        if len(search_terms) != 0:
            sql_search += ' AND '.join(
                '='.join((key, "'{}'".format(value))) for key, value in
                search_terms.items())
        sql_search += ';'

    # create SQL connection
    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    # execute and return sql search
    return sql_database.get_data(sql_search)


def sign_history():

    all_signs = []
    all_signs.extend(search_signs('sign out', {}))
    all_signs.extend(search_signs('sign in', {}))
    return sorted(all_signs, key=lambda x: datetime.strptime('{} {}'.format(x[1], x[2]), '%Y-%m-%d %H:%M:%S'), reverse=True)


def search_users(search_terms):
    """Searches the user tables with the dictionary provided in args."""

    # if no terms are provided, return all users
    if len(search_terms) != 0:
        sql_search = "SELECT * FROM users WHERE "
        # takes keys, values, formats value, joins them with '=', and then
        # adds AND between dict keys adds ; to end sql statement
        sql_search += ' AND '.join(
            '='.join((key, "'{}'".format(value))) for key, value in
            search_terms.items()) + ';'
    else:
        sql_search = "SELECT * FROM users;"

    # create SQL connection
    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    # execute and return sql search
    return sql_database.get_data(sql_search)


def edit_user(user_id, edited_terms):

    sql_statement = """UPDATE users """ \
                    """SET """
    sql_statement += ', '.join('='.join((key, "'{}'".format(value))) for key, value in
                                  edited_terms.items()) + f' WHERE id = {user_id};'
    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    sql_database.insert_data(sql_statement)


def delete_user(user_id):

    sql_statement = f"""DELETE FROM users WHERE id = {user_id};"""

    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    sql_database.insert_data(sql_statement)


def edit_sign_in(sign_in_id, edited_terms):
    
    sql_statement = 'UPDATE sign_in SET '
    sql_statement += ', '.join('='.join((key, "'{}'".format(value))) 
                               for key, value in edited_terms.items()) + f' WHERE sign_in_id = {sign_in_id};'
    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    sql_database.insert_data(sql_statement)


def delete_sign_in(sign_in_id):

    sql_statement = f'DELETE FROM sign_in WHERE sign_in_id = {sign_in_id}'
    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    sql_database.insert_data(sql_statement)


def edit_sign_out(sign_out_id, edited_terms):

    sql_statement = 'UPDATE sign_out SET '
    sql_statement += ', '.join('='.join((key, "'{}'".format(value))) 
                               for key, value in edited_terms.items()) + f' WHERE sign_out_id = {sign_out_id};'
    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    sql_database.insert_data(sql_statement)


def delete_sign_out(sign_out_id):

    sql_statement = f'DELETE FROM sign_out WHERE sign_out_id = {sign_out_id}'
    print(sql_statement)
    sql_database = SQL_interface.sqlInterface('test.db')
    sql_database.create_connection()
    sql_database.insert_data(sql_statement)