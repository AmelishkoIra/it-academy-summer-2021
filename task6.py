"""
Вводится число, найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4).
"""


def max_divisor(number):
    exponent = 0
    while 2 ** exponent <= number:
        if number % (2 ** exponent) == 0:
            divisor = (2 ** exponent)
            exponent = exponent + 1
        else:
            break
    print("Наибольший общий делитель: ", divisor)

    
max_divisor(10)
