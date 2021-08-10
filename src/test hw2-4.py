import unittest
import ddt
import task1_hw2


@ddt.ddt
class Test_long_word(unittest.TestCase):

    @ddt.data(
        ("Hello girl", "Hello"),
        ("I like sun", "like"),
        ("My number 999999999", "999999999")
    )

    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw2.long_word(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (4446, AttributeError),
        ({}, AttributeError),
        ([], AttributeError),
        ("", ValueError),
    )

    @ddt.unpack
    def test_errors(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw2.long_word(input_data)
