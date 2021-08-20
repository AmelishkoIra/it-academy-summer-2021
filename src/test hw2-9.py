"""
тест на функцию area_triangle, которая расчитывает
площадь треугольника.
"""

import ddt
import task1_hw2
import unittest


@ddt.ddt
class TestAreaTriangle(unittest.TestCase):

    @ddt.data(
        (3, 4, 5, "Площадь треугольника равно 6.0"),
        (1, 4, 5, "Неверные данные"),
        (5, 5, 5, "Площадь треугольника равно 10.825317547305483")
    )
    @ddt.unpack
    def test_value(self, a, b, c, expected):
        """позитивный тест"""
        result = task1_hw2.area_triangle(a, b, c)
        self.assertEqual(result, expected)

    @ddt.data(
        ([5], [5], [5], TypeError),
        ({5}, [5], [5], TypeError),
        ("5", "9", "8", TypeError),
    )
    @ddt.unpack
    def test_errors(self, a, b, c, expected):
        """негативный тест"""
        with self.assertRaises(expected):
            task1_hw2.area_triangle(a, b, c)
