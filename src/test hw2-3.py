import unittest
import ddt
import task1_hw2


@ddt.ddt
class Test_func_sum(unittest.TestCase):

    @ddt.data(
        (2, 2, 2, (4, 4)),
        (5, 8, 12, (60, 96)),
        (10, 4, 67, (672, 68)),
    )

    @ddt.unpack
    def test_value(self, price_rub, price_kop, product, final_price):
        result = task1_hw2.func_sum(price_rub, price_kop, product)
        self.assertEqual(result, final_price)


    @ddt.data(
        (10, 3, [3], TypeError),
        ("10", "5", "98", OverflowError),
        ([2], [4], [67], TypeError),
        ({2}, {9}, {89}, TypeError),
    )

    @ddt.unpack
    def test_errors(self, price_rub, price_kop, product, final_price):
        with self.assertRaises(final_price):
            task1_hw2.func_sum(price_rub, price_kop, product)
