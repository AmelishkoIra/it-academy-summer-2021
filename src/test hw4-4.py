import ddt
import task1_hw4
import unittest


@ddt.ddt
class Test_lists_dif(unittest.TestCase):

    @ddt.data(
        ({4, 9, 0}, {4, 7, 3}, 4),
        ({3}, {6}, 2),
    )
    @ddt.unpack
    def test_value(self, input_data1, input_data2, expected):
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
        with self.assertRaises(expected):
            task1_hw4.compare_lists_difference(input_data1, input_data2)
