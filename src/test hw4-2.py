import ddt
import task1_hw4
import unittest


@ddt.ddt
class Test_euclidean_algorithm(unittest.TestCase):

    @ddt.data(
        (5, 2, "Наибольший общий делитель: 1"),
        (9, 18, "Наибольший общий делитель: 9"),
        (25, 5, "Наибольший общий делитель: 5")
    )
    @ddt.unpack
    def test_value(self, input_data1, input_data2, expected):
        result = task1_hw4.euclidean_algorithm(input_data1, input_data2)
        self.assertEqual(result, expected)

    @ddt.data(
        ("2", "4", TypeError),
        ([2, 3], [3], TypeError),
        ({3}, {3}, TypeError),
        ({3:5}, {5:15}, TypeError),
    )
    @ddt.unpack
    def test_error(self, input_data1, input_data2, expected):
        with self.assertRaises(expected):
            task1_hw4.euclidean_algorithm(input_data1, input_data2)
