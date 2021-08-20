"""
тест на функцию round_number, которая определяет,
сколько кругляшей в числе. 
"""
import ddt
import task1_hw2
import unittest


@ddt.ddt
class TestRoundNumber(unittest.TestCase):

    @ddt.data(
        ("456", 1),
        ("88", 4),
        ("998", 4),
        ("", 0),
    )
    @ddt.unpack
    def test_value(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw2.round_numbers(input_data)
        self.assertEqual(result, expected)

    def test_errors(self):
        """негативный тест"""
        with self.assertRaises(TypeError):
            task1_hw2.round_numbers(444)
