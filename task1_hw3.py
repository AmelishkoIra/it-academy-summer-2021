"""Функции из Homework3 для тестирования"""


def fizzbuzz(number):
    """
    Функция печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
    вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных
    и 3 и 5 - FizzBuzz.
    """
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        return "FizzBuzz"
    elif int(number) % 3 == 0:
        return "Fizz"
    elif int(number) % 5 == 0:
        return "Buzz"
    else:
        return number


def number_of_pairs(number):
    """
    Функция считает, сколько в списке пар элементов, равных друг другу.
    Входные данные - строка из чисел, разделенная пробелами. Выходные данные -
    количество пар.
    """
    number_without_spaces = number.split(" ")
    ist_of_number = [int(s) for s in number_without_spaces]
    couples = 0
    for i in range(len(ist_of_number)):
        for j in range(i + 1, len(ist_of_number)):
            if ist_of_number[i] == ist_of_number[j]:
                couples += 1
    return "{} пары чисел".format(couples)


def meet_once_element(lst):
    """
    Функция выводит элементы списка, которые встречаются только один раз.
    Элементы выводятся в том порядке, в котором они встречаются в списке.
    """

    lst_new = ""
    for i in lst:
        if lst.count(i) <= 1:
            if str(i) not in lst_new:
                lst_new += str(i)
    return lst_new


def separation_zero(lst):
    """
    Функция перемещает все ненулевые элементы списка в левую часть списка, не
    меняя их порядок, а все нули - в правую часть.
    """

    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst
