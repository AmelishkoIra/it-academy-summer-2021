"""тест функции compare_lists_difference.
Функция считает, сколько различных чисел входит только в один из списков.
"""

import ddt
import task1_hw4
import unittest


@ddt.ddt
class TestListsDif(unittest.TestCase):

    @ddt.data(
        ({4, 9, 0}, {4, 7, 3}, 4),
        ({3}, {6}, 2),
    )
    @ddt.unpack
    def test_value(self, input_data1, input_data2, expected):
        """позитивный тест"""
        result = task1_hw4.compare_lists_difference(input_data1, input_data2)
        self.assertEqual(result, expected)

    @ddt.data(
        ("4, 9, 0", "4, 7, 3", TypeError),
        ([4, 9, 0], [4, 7, 3], TypeError),
        (456, 478, TypeError),
        ({}, {}, TypeError),
    )
    @ddt.unpack
    def test_error(self, input_data1, input_data2, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw4.compare_lists_difference(input_data1, input_data2)
