"""
Написать программу которая находит ближайшую степень двойки к введенному
числу. 10(8), 20(16), 1(1), 13(16)
"""


def input_number(a):
    for i in range(0, 1000):
        if 2 ** i >= a:
            if 2 ** i - a > a - 2 ** (i - 1):
                print(2 ** (i - 1))
                break
            else:
                print(2 ** i)
                break

                
input_number(10)
