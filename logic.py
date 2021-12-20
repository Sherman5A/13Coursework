import SQL_interface_2
import re
from datetime import datetime

def create_user(account_variables):
    """"Create a new user, performs validation, then adds to sql table"""

    def user_validation(account_variables):
        """Performs len_check, string_check, and password repeat check"""
        for key, value in account_variables.items():
            if validation.len_check() == False:
                return False, key, 'Length check'
            if key == 'first_name' or key == 'second_name':
                if validation.string_check(value) == False:
                    return False, key, 'Alpha check'

        if account_variables['password'] == account_variables['password_repeat']:
            return False, 'password', "Passwords don't match"
        
        return True, None, None   


    user_validation_results = user_validation(account_variables)
    if user_validation_results[0] == False:
        return user_validation_results

    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS users (
                                    id integer PRIMARY KEY,
                                    first_name text NOT NULL,
                                    second_name text NOT NULL,
                                    year_group text NOT NULL,
                                    form_group text NOT NULL,
                                    username text NOT NULL,
                                    password text NOT NULL
                                ); """


    sql_interface = SQL_interface_2.SQL_inter('test.db')
    sql_interface.create_connection()
    sql_interface.execute_sql(sql_create_user_table)


def check_login_creds(input_username, input_password):
    pass



class validation():
    """Class containing validation"""
    
    def string_check(input):
        """Checks if a string contains digits or special characters"""
    
        regex_arguement = re.compile('\d+|[@;:()]')
        try:
            regex_return = re.search(regex_arguement, input)    
            if regex_return:
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
            min_num: optionial, input can not be lower than value"""
        try:
            converted_input = int(input)
            if min_num == None:
                return True
            return converted_input > min_num
        except ValueError:
            return False

    def password_strength(input):
        """Check password is >= 7 characters, contains lower and upper case """
        if len(input) < 7:
            return False

        if input.isupper() == False and input.islower() == False:
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
