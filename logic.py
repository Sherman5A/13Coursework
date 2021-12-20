import SQL_interface_2
import re
from datetime import datetime

def create_user(account_variables):

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


def user_validation(account_variables):

    for key, value in account_variables.items():
        if validation.len_check() == False:
            return False, key, 'Length check'
        if key == 'first_name' or key == 'second_name':
            if validation.string_check(value) == False:
                return False, key, 'Alpha check'

    if account_variables['password'] == account_variables['password_repeat']:
        return False, 'password', "Passwords don't match"
        

def check_login_creds(input_username, input_password):
    pass



class validation():
    
    def string_check(input):
    
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
        if len(input) <= 0 or len(input) > max_len:
            return False
        return True


    def validate_num(input, min_num=None):
        try:
            converted_input = int(input)
            if min_num == None:
                return True
            return converted_input > min_num
        except ValueError:
            return False

    def password_strength(input):

        if len(input) < 7:
            return False

        if input.isupper() == False and input.islower() == False:
            return True
        return False

def get_date_time():

    unformatted_datetime = datetime.now()
    date_str = unformatted_datetime.strftime('%d/%m/%Y')
    time_str = unformatted_datetime.strftime('%H:%M:%S')
    return date_str, time_str


def sign_in_school():
     date_str, time_str = get_date_time()
