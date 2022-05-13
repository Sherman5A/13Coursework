import re
from datetime import datetime


def date_format_check(input):
    """Validate dates using the %Y-%m-%d format."""
    
    try:
        # Try to convert time from string in the format YYYY:MM:DD e.g 2009:11:22
        datetime.strptime(input, '%Y-%m-%d')
        return True
    # If there is an error in converting, either due to an impossible date,
    # or a formatting error, return false
    except ValueError:
        return False

def time_format_check(input):
    """Validate times using the %H:%M:%S format."""
    
    try:
        # Try to convert time from string in the format HH:MM:SS e.g 17:49:22
        datetime.strptime(input, '%H:%M:%S')
        return True
    # If there is an error in converting, either due to an
    # impossible time, or a formatting error, return false.
    except ValueError:
        return False


def string_check(input):
    """Check that the inputs do not contain digits or symbols."""
    
    # Use recursion to iterate through each element of the string.
    def recursion(i):
   
        try:
            regex_result = re.match(regex_argument, input[i])
            # Terminating condition.
            if i == len_input-1:
                return True
            elif regex_result:
                return False
            # Continue iterating through.
            else:
                return recursion(i+1)
        # If an index of input is not a string, return false.
        except TypeError:
            return False

    # Try to search the string with regex. If the input is not a string data type
    # a type error flag will be raised, triggering the except, returning false.
    regex_argument = re.compile('\d|[@;^&{}:\[\]()+=_`¬~#]')
    
    # Try to get the length of the input.
    try: 
        len_input = len(input)
        return recursion(0)
    # If the input is the wrong type, return false.
    except TypeError:
        return False

   
def len_check(input, max_len):
    """Checks length of compatible data type
        input: variable to check
        max_len: int maximum length to return true
    """
    try:
        if len(input) <= 0 or len(input) > max_len:
            return False
        return True
    # Try to get the length of input. If the len can not be called on the
    # data type, a type error flag will be raised,
    # triggering the except, returning false.
    except TypeError:
        return False


def validate_num(input, min_num=None):
    """Checks if input is int
        input: variable to check
        min_num: optional, input can not be lower than value
    """

    try:
        converted_input = int(input)
        if min_num is None:
            return True
        return converted_input > min_num
    # Try to convert the input to an integer.
    # If the input can not converted due to non-digits, a
    # value error flag will be raised,
    # triggering the except, returning false.
    except ValueError:
        return False


def password_strength(input):
    """Check password is > 7 characters, contains lower and upper case.
       Returns true if password check is passed, false otherwise."""

    if len(input) < 7:
        return False

    # Check if password contains both lower and upper case characters.
    # Setting flags for the check
    upper_flag = True
    lower_flag = False

    # Checking each letter
    for i in input:
        if i.isupper() == True:
            upper_flag = True
        if i.islower() == True:
            lower_flag = True
    
    # Return false, true depending on the flags
    if upper_flag == False:
        return False
    if lower_flag == False:
        return False
    else:
        return True
