import ddt
import task1_hw2
import unittest


@ddt.ddt
class Test_password(unittest.TestCase):

    @ddt.data(
        ("000010", "Пароль не подходит"),
        ("0000010", "Пароль подходит по длине"),
        ("wellwellwell", "Пароль подходит по длине")
    )
    @ddt.unpack
    def test_1(self, input_data, expected):
        result = task1_hw2.password_verification(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (123, TypeError),
    )
    @ddt.unpack
    def test_2(self, input_data, expectes):
        with self.assertRaises(expectes):
            task1_hw2.password_verification(input_data)
            
