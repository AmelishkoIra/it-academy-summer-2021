import ddt
import task1_hw2
import unittest


@ddt.ddt
class Test_continuous_chain(unittest.TestCase):

    @ddt.data(
        ("000010", 4),
        ("0000010", 5),
        ("00111101000", 3)
    )
    @ddt.unpack
    def test_1(self, input_data, expected):
        result = task1_hw2.continuous_chain(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (10001, AttributeError),
        ([100], AttributeError),
        ({100}, AttributeError),
    )
    @ddt.unpack
    def test_2(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw2.continuous_chain(input_data)
