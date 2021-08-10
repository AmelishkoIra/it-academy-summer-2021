import ddt
import task1_hw4
import unittest


@ddt.ddt
class Test_different_words(unittest.TestCase):

    @ddt.data(
        ("Hello world", 2),
        ("Ron is a boy", 4),
        ("well well well", 1)
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw4.counting_different_words(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (123, AttributeError),
        ([1, 2, 3], AttributeError),
        ({1, 2, 3}, AttributeError),
        ({1: 5}, AttributeError),
    )
    @ddt.unpack
    def test_error(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw4.counting_different_words(input_data)
