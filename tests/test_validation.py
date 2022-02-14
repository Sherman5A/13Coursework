from src import validation
import unittest


class TestDateCheck(unittest.TestCase):

    def test_wrong_format(self):
        incorrect_format = '14-02-2022'
        result = validation.date_format_check(incorrect_format)
        self.assertFalse(result)

    def test_date_exists(self):
        incorrect_date  = '2022-02-31'
        result = validation.date_format_check(incorrect_date)
        self.assertFalse(result)

    def test_correct_format_time(self):
        correct_time_format = '2022-02-14'
        result = validation.date_format_check(correct_time_format)
        self.assertTrue(result)


class TestTimeCheck(unittest.TestCase):

    def test_wrong_format(self):
        incorrect_format = '23.32.54.32'
        result = validation.time_format_check(incorrect_format)
        self.assertFalse(result)

    def test_time_exists(self):
        incorrect_time = '25:14:40'
        result = validation.time_format_check(incorrect_time)
        self.assertFalse(result)

    def test_correct_format_time(self):
        correct_time_format = '12:32:53'
        result = validation.time_format_check(correct_time_format)
        self.assertTrue(result)


class TestStringCheck(unittest.TestCase):

    def test_integer(self):
        integer = 123
        result = validation.string_check(integer)
        self.assertFalse(result)

    def test_string_digits(self):
        string_digits = '123'
        result = validation.string_check(string_digits)
        self.assertFalse(result)

    def test_symbols(self):
        string_symbols = '#@:"{}[]&()+_=^'
        result = validation.string_check(string_symbols)
        self.assertFalse(result)

    def test_correct_string(self):
        correct_string = 'hello fnfk oe'
        result = validation.string_check(correct_string)
        self.assertTrue(result)


class TestLenCheck(unittest.TestCase):

    def test_less_equal_0(self):
        string = ''
        result = validation.len_check(string, 20)
        self.assertFalse(result)

    def test_greater_max(self):
        string = '12345678910'
        result = validation.len_check(string, 10)
        self.assertFalse(result)

    def test_correct_len(self):
        correct_string = '1234'
        result = validation.len_check(correct_string, 5)
        self.assertTrue(result)


class TestValidateNum(unittest.TestCase):

    def test_string(self):
        string = ''
        result = validation.validate_num(string)
        self.assertFalse(result)

    def test_greater_min_num(self):
        integer = 12
        result = validation.validate_num(integer, 13)
        self.assertFalse(result)

    def test_correct_number(self):
        integer = 13
        result = validation.validate_num(integer, 12)
        self.assertTrue(result)


class TestPasswordStrength(unittest.TestCase):

    def test_length(self):
        string = '123456'
        result = validation.password_strength(string)
        self.assertFalse(result)

    def test_upper_lowercase(self):
        string = '@@@@&*&%$&@^^##$%(){}'
        result = validation.password_strength(string)
        self.assertFalse(result)

    def test_strong_password(self):
        string = 'abcABCabc'
        result = validation.password_strength(string)
        self.assertTrue(result)

        
