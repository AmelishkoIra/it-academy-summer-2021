"""
тест на функцию palindrom, которая определяет,
является ли число палиндромом.
"""

import ddt
import task1_hw2
import unittest


@ddt.ddt
class TestPalindrom(unittest.TestCase):

    @ddt.data(
        (777, True),
        (32, False),
        (23, False),
        ("333", True),
        ("cooK", False),
        ({4}, False)
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw2.palindrom(input_data)
        self.assertEqual(result, expected)
