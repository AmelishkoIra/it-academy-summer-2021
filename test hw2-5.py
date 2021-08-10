import unittest
import ddt
import task1_hw2


@ddt.ddt
class Test_del_space(unittest.TestCase):

    @ddt.data(
        ("Hello girl", "helogir"),
        ("I like cook", "ilkeco"),
        ("My number 999", "mynuber9")
    )

    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw2.del_space(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (4446, AttributeError),
        ({333}, AttributeError),
        ([333], AttributeError),
    )

    @ddt.unpack
    def test_errors(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw2.del_space(input_data)