"""
тест на функцию continuous_chain, которая нахождит 
самую длинную цепочку нулей и выводит ее длину.
"""
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
    def test_value(self, input_data, expected):
        """позитивный тест"""
        result = task1_hw2.continuous_chain(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (10001, AttributeError),
        ([100], AttributeError),
        ({100}, AttributeError),
    )
    @ddt.unpack
    def test_erorr(self, input_data, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw2.continuous_chain(input_data)
