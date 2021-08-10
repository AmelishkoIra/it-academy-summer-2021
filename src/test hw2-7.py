import unittest
import ddt
import task1_hw2


@ddt.ddt
class Test_fibonacci(unittest.TestCase):

    @ddt.data(
        (7, "8"),
        (3, "1"),
        (23, "17711"),
    )

    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw2.fibonacci(input_data)
        self.assertEqual(result, expected)


    @ddt.data(
        ("", TypeError),
        ([2], TypeError),
        ({2}, TypeError),
    )

    @ddt.unpack
    def test_errors(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw2.func_sum(input_data)