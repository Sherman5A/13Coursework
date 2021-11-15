import SQL_interface_2
import re
from datetime import datetime


def check_login_creds(input_username, input_password):
    pass


def get_date_time():

    unformatted_datetime = datetime.now()
    date_str = unformatted_datetime.strftime('%d/%m/%Y')
    time_str = unformatted_datetime.strftime('%H:%M:%S')
    return date_str, time_str


def sign_in_school():

     date_str, time_str = get_date_time()


def validate_alpha(input):
    
    regex_arguement = re.compile('\d+|[@;:()]')
    try:
        regex_return = re.search(regex_arguement, input)    
        if regex_return:
            return False
        return True
    except TypeError:
        print('Variable is not string')
    

def validate_num(input, min_num=None):
    try:
        converted_input = int(input)
        if min_num == None:
            return True
        return converted_input > min_num
    except ValueError:
        return False


def validate_date(input):
    pass