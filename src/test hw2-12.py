"""
тест функции bus, которая считает колличесиво автобусов
для поездки.
"""
import ddt
import task1_hw2
import unittest


@ddt.ddt
class TestBus(unittest.TestCase):

    @ddt.data(
        (2, 4, 5, "необходимо 2 автобусa"),
        (9, 1, 5, "поездка не состоится"),
        (9, 6, 5, "необходимо 3 автобусa"),
    )
    @ddt.unpack
    def test_value(self, input_data1, input_data2, input_data3, expected):
        """позитивный тест"""
        result = task1_hw2.bus(input_data1, input_data2, input_data3)
        self.assertEqual(result, expected)

    @ddt.data(
        ("4", "3", "8", TypeError),
        ([5], "3", "8", TypeError),
        ({5}, [3], [8], TypeError),
        (3, 7, 0, ZeroDivisionError),
    )
    @ddt.unpack
    def test_errors(self, input_data1, input_data2, input_data3, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw2.bus(input_data1, input_data2, input_data3)
