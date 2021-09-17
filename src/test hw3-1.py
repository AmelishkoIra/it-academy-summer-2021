"""
тест на функцию fizzbuzz, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный
5 пишет Buzz, а вместо чисел одновременно кратных
и 3 и 5 - FizzBuzz.
"""

import ddt
import task1_hw3
import unittest


@ddt.ddt
class TestFizzbuzz(unittest.TestCase):

    @ddt.data(
        (15, "FizzBuzz"),
        (9, "Fizz"),
        (25, "Buzz"),
        (11, 11),
        ("2", "2"),
    )
    @ddt.unpack
    def test_1(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw3.fizzbuzz(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ("", ValueError),
        ("well", ValueError),
        ([1], TypeError),
        ({3}, TypeError),
        ((11, 12), TypeError),
    )
    @ddt.unpack
    def test_2(self, input_data, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw3.fizzbuzz(input_data)
