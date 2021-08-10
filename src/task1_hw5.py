"""Функции из Homework5 для тестирования"""


def input_number(a):
    """
    Написать программу которая находит ближайшую степень двойки к введенному
    числу.
    """
    for i in range(0, 1000):
        if 2 ** i >= a:
            if 2 ** i - a > a - 2 ** (i - 1):
                return 2 ** (i - 1)
                break
            else:
                return 2 ** i
                break


def max_divisor(number):
    """
    Вводится число, найти его максимальный делитель, являющийся степенью
    двойки.
    """
    exponent = 0
    while 2 ** exponent <= number:
        if number % (2 ** exponent) == 0:
            divisor = (2 ** exponent)
            exponent = exponent + 1
        else:
            break
    return divisor
