import re
from datetime import datetime

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
            "INSERT INTO users(first_name, second_name, year_group, form_group, username, password) VALUES(?, ?, ?, ?, ?, ?);",
            (
                account_variables['first_name'],
                account_variables['second_name'],
                account_variables['year_group'],
                account_variables['form_group'], account_variables['username'],
                account_variables['password']))

    # validation
    for key, value in account_variables.items():

        # if value is empty or above 20 characters, decline
        if not validation.len_check(value, 20):
            return False, key, 'Length check, check field is not empty and is under 20 characters '

        # names require string checks as no symbols should be accepted
        if key == 'first_name' or key == 'second_name':
            if not validation.string_check(value):
                return False, key, 'Alpha check'

    # check if passwords match           
    if account_variables['password'] != account_variables['password_repeat']:
        return False, 'password', "Passwords don't match"

    # check if password is strong enough
    if not validation.password_strength(account_variables['password']):
        return False, 'password', 'Password not strong enough. Use >= 7 characters and both upper and lower case letters'

    create_table()

    # check for duplicate usernames. Usernames must be unique as they are
    # used to log in
    common_usernames = sql_database.get_data(
        "SELECT username FROM users WHERE username=?",
        (account_variables['username'],))
    if len(common_usernames) != 0:
        return False, 'username', 'Username is not unique'

    write_user()
    return True  # returns everything successful flag

def create_sign_in():

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

    sql_database.insert_data("INSERT INTO sign_in(date_time, student_id) VALUES(date('now'), time('now'), ?)", '2')

def create_sign_out(sign_out_type):

    # creating class interfaces, passing in db to connect to
    sql_database = SQL_interface.sqlInterface('test.db')
    # create connection to database
    sql_database.create_connection()

    sql_create_table = """CREATE TABLE IF NOT EXISTS sign_out (
        "sign_out_id" INTEGER,
        "date" TEXT NOT NULL,
        "time" TEXT NOT NULL,
        "sign_out_type" TEXT NOT NULL,
        "student_id" INTEGER NOT NULL,
        FOREIGN KEY("student_id") REFERENCES "users"("id") ON UPDATE CASCADE ON DELETE CASCADE,
        PRIMARY KEY("sign_out_id" AUTOINCREMENT)
        );"""

    sql_database.create_table(sql_create_table)
    sql_database.insert_data("INSERT INTO sign_out(date_time, sign_out_type, student_id) VALUES(date('now'), time('now'), ?, ?)", (sign_out_type, '2'))

def search_signs(search_terms):

    if len(search_terms) != 0:
        sql_search = 'SELECT * FROM sign_in, sign_out'
    else:
        if search_terms['sign_type'] == 'both' or search_terms['sign_type'] == '':
            sql_search = "SELECT * FROM sign_in, sign_out WHERE "
        elif search_terms['sign_type'] == 'sign in':
            sql_search = "SELECT * FROM sign_in WHERE"
        else:
            sql_search = "SELECT * FROM sign_out WHERE"

        sql_search += ' AND '.join('='.join((key, "'{}'".format(value))) for key, value in search_terms.items()) + ';'
    print(sql_search)


def check_login_creds(input_username, input_password):
    pass


def search_users(search_terms):
    """Searches the user tables with the dictonary provided in args"""

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


class validation():
    """Class containing validation"""

    def string_check(input):
        """Checks if a string contains digits or special characters"""

        # create regex searching for digits and symbols
        regex_argument = re.compile('\d+|[@;:()]')
        try:
            regex_return = re.search(regex_argument, input)
            if regex_return:  # string contains symbols or digits
                return False
            return True
        except TypeError:
            print('Variable is not string')
            return False

    def len_check(input, max_len):
        """Checks length of string
            input: variable to check
            max_len: int maximum length to return true
        """

        if len(input) <= 0 or len(input) > max_len:
            return False
        return True

    def validate_num(input, min_num=None):
        """Checks if input is int
            input: variable to check
            min_num: optionial, input can not be lower than value
        """

        try:
            converted_input = int(input)
            if min_num is None:
                return True
            return converted_input > min_num
        except ValueError:
            return False

    def password_strength(input):
        """Check password is >= 7 characters, contains lower and upper case """

        if len(input) < 7:
            return False

        # contains both lower and upper case characters
        if input.isupper() is False and input.islower() is False:
            return True
        return False


def get_date_time():
    """Returns date and time"""

    unformatted_datetime = datetime.now()
    date_str = unformatted_datetime.strftime('%d/%m/%Y')
    time_str = unformatted_datetime.strftime('%H:%M:%S')
    return date_str, time_str


def sign_in_school():
    date_str, time_str = get_date_time()
