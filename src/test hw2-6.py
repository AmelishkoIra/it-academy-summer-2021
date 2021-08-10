import ddt
import task1_hw2
import unittest


@ddt.ddt
class Test_letter_count(unittest.TestCase):

    @ddt.data(
        ("Hello girl", (8, 1)),
        ("I like sun", (7, 1)),
        ("My number 999999999", (7, 1)),
        ({}, (0, 0)),
        ([], (0, 0)),
        ("", (0, 0))
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw2.letter_count(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (4446, TypeError),
        ({3}, TypeError),
    )
    @ddt.unpack
    def test_errors(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw2.letter_count(input_data)
