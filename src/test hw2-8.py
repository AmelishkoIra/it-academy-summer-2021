import ddt
import task1_hw2
import unittest


@ddt.ddt
class Test_palindrom(unittest.TestCase):

    @ddt.data(
        (777, True),
        (32, False),
        (23, False),
        ("333", True),
        ("cooK", False),
        ({4}, False)
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw2.palindrom(input_data)
        self.assertEqual(result, expected)
