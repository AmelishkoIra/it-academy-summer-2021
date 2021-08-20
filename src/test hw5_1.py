"""тест функции input_number.
функция находит ближайшую степень 2 к введенному числу.
"""

import ddt
import task1_hw5
import unittest


@ddt.ddt
class TestInputNumber(unittest.TestCase):

    @ddt.data(
        (34, 2),
        (45, 1),
        (999, 1),
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw5.max_divisor(input_data)
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
            task1_hw5.max_divisor(input_data)
