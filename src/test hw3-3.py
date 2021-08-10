import ddt
import task1_hw3
import unittest


@ddt.ddt
class Test_number_pairs(unittest.TestCase):

    @ddt.data(
        ("22 34 22", "1 пары чисел"),
        ("33 33 33 67", "3 пары чисел"),
        ("66 78 95", "0 пары чисел")
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        result = task1_hw3.number_of_pairs(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (222334, AttributeError),
        ([22, 77, 8], AttributeError),
        ("22 well 67", ValueError),
        ({34, 67, 67}, AttributeError),
        ({2:6}, AttributeError),
        ("", ValueError),
    )
    @ddt.unpack
    def test_error(self, input_data, expected):
        with self.assertRaises(expected):
            task1_hw3.number_of_pairs(input_data)
