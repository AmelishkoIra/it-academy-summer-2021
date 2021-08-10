import ddt
import task1_hw3
import unittest


@ddt.ddt
class Test_meet_element(unittest.TestCase):

    @ddt.data(
        ([3, 4, 4, 5], "35"),
        ("1, 4, 5", "145"),
        ([5, 5, 5, 9], "9")
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw3.meet_once_element(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ({3, 6, 6, 4}, AttributeError),
        (678, TypeError),
        ({5:8}, AttributeError),
    )
    @ddt.unpack
    def test_errors(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw3.meet_once_element(input_data)
