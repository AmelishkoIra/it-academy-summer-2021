import unittest
import ddt
import task1_hw5

@ddt.ddt
class Test_input_number(unittest.TestCase):

    @ddt.data(
        (34, 2),
        (45, 1),
        (999, 1),
    )

    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw5.max_divisor(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ({34}, TypeError),
        ([9], TypeError),
        ({3:2}, TypeError),
        ("32", TypeError),
    )

    @ddt.unpack
    def test_errors(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw5.max_divisor(input_data)