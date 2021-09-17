"""
тест на функцию long_word, которая Находит самое
длинное слово в предложении.
"""
import ddt
import task1_hw2
import unittest


@ddt.ddt
class TestLongWord(unittest.TestCase):

    @ddt.data(
        ("Hello girl", "Hello"),
        ("I like sun", "like"),
        ("My number 999999999", "999999999")
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw2.long_word(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (4446, AttributeError),
        ({}, AttributeError),
        ([], AttributeError),
        ("", ValueError),
    )
    @ddt.unpack
    def test_errors(self, input_data, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw2.long_word(input_data)
