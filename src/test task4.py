import ddt
import task4
import unittest


@ddt.ddt
class Test_modular_inverses(unittest.TestCase):
    """Test of modular inverses"""

    @ddt.data(
        (3, 200, 8967),
        (2, 1000, 278049),
        (3, 20000, 132759233),
    )
    @ddt.unpack
    def test_value(self, input_start, input_finish, expected):
        """Test of input values"""
        result = task4.modular_inverses(input_start, input_finish)
        self.assertEqual(result, expected)

    @ddt.data(
        ("1", "2000", TypeError),
        ([3], [2000], TypeError),
        ({3}, {2000}, TypeError),
        ({2: 2}, 200, TypeError),
    )
    @ddt.unpack
    def test_error(self, input_start, input_finish, expected):
        """Test of errors"""
        with self.assertRaises(expected):
            task4.modular_inverses(input_start, input_finish)

if __name__ == '__main__':
    unittest.main()
