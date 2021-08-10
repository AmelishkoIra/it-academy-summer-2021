"""Функции из Homework5 для тестирования"""


def input_number(a):
    """Функция находит ближайшую степень 2 к введенному числу."""
    for i in range(0, 1000):
        if 2 ** i >= a:
            if 2 ** i - a > a - 2 ** (i - 1):
                return 2 ** (i - 1)
                break
            else:
                return 2 ** i
                break


def max_divisor(number):
    """Функция максимальный делитель.

    Дано число. Функция находит находит максимальный делитель этого числа,
    являющийся степенью двойки.
    """
    exponent = 0
    while 2 ** exponent <= number:
        if number % (2 ** exponent) == 0:
            divisor = (2 ** exponent)
            exponent = exponent + 1
        else:
            break
    return divisor
