import re
from datetime import datetime


def date_format_check(input):
    try:
        # Try to convert time from string in the format YYYY:MM:DD e.g 2009:11:22
        datetime.strptime(input, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def time_format_check(input):
    try:
        # Try to convert time from string in the format HH:MM:SS e.g 17:49:22
        datetime.strptime(input, '%H:%M:%S')
        return True
    except ValueError:
        return False


def string_check(input):
    """Checks if a string contains digits or special characters"""

    # create regex searching for digits and symbols
    regex_argument = re.compile('\d+|[@;:()+=_`¬~#]')
    try:
        regex_result = re.search(regex_argument, input)
        if regex_result:  # string contains symbols or digits
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
    """Check password is > 7 characters, contains lower and upper case.
       Returns true if password check is passed, false otherwise."""

    if len(input) < 7:
        return False

    # Check if password contains both lower and upper case characters.
    upper_flag = True
    lower_flag = False
    for i in input:
        print(i)
        if i.isupper() == True:
            print('capital')
            upper_flag = True
        if i.islower() == True:
            lower_flag = True
    if upper_flag == False:
        return False
    if lower_flag == False:
        return False
    else:
        return True
