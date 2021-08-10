import ddt
import task1_hw3
import unittest


@ddt.ddt
class Test_separation_zero(unittest.TestCase):

    @ddt.data(
        ([3, 4, 4, 0, 5, 9], [3, 4, 4, 5, 9, 0]),
        ([6, 9, 0, 0, 7], [6, 9, 7, 0, 0]),
        ([6, 9, 7, 0, 0], ['7', 9, 0, 0]),
        ([[3, 0, 9], 0, 4, 7, 0], [[3, 0, 9], 4, 7, 0, 0]),
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw3.separation_zero(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ({3, 6, 6, 4}, AttributeError),
        ({3, "5", 0, 9}, AttributeError),
    )
    @ddt.unpack
    def test_errors(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw3.separation_zero(input_data)
