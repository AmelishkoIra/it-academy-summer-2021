"""
тест на функцию fibonacci, которая выводит 
n-ое число Фибоначчи.
"""
import ddt
import task1_hw2
import unittest


@ddt.ddt
class TestFibonacci(unittest.TestCase):

    @ddt.data(
        (7, "8"),
        (3, "1"),
        (23, "17711"),
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw2.fibonacci(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ("", TypeError),
        ([2], TypeError),
        ({2}, TypeError),
    )
    @ddt.unpack
    def test_errors(self, input_data, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw2.func_sum(input_data)
