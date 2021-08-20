"""
тест на функцию first_word, которая находит
первое слово в строке
"""
import ddt
import task1_hw2
import unittest


@ddt.ddt
class Test_first_word(unittest.TestCase):

    @ddt.data(
        ("Hello guys", ["Hello"]),
        ("I like sun", ["I"]),
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw2.first_word(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (444, AttributeError),
        ([5], AttributeError),
        ({7}, AttributeError),
    )
    @ddt.unpack
    def test_errors(self, input_data, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw2.first_word(input_data)
