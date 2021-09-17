"""тест функции max_divisor.
Функция находит находит максимальный делитель этого числа,
являющийся степенью двойки.
"""

import ddt
import task1_hw5
import unittest


@ddt.ddt
class TestMaxDivisor(unittest.TestCase):

    @ddt.data(
        (34, 32),
        (45, 32),
        (999, 1024),
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw5.input_number(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ({34}, TypeError),
        ([9], TypeError),
        ({3: 2}, TypeError),
        ("32", TypeError),
    )
    @ddt.unpack
    def test_errors(self, input_data, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw5.input_number(input_data)
