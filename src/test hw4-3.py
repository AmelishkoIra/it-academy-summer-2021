import ddt
import task1_hw4
import unittest


@ddt.ddt
class Test_compare_lists(unittest.TestCase):

    @ddt.data(
        ({4, 9, 0}, {4, 7, 3}, 1),
        ({3}, {6}, 0),
    )
    @ddt.unpack
    def test_value(self, input_data1, input_data2, expected):
        result = task1_hw4.compare_lists(input_data1, input_data2)
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
            task1_hw4.compare_lists(input_data1, input_data2)
