"""функции из Homework4 для тестирования"""


def compare_lists(list_one, list_two):
    """Функция сравнения списков.

    Функция считает, сколько различных чисел содержится одновременно как в
    первом списке, так и во втором.
    """
    compare = list_one & list_two
    return len(compare)


def compare_lists_difference(list_one, list_two):
    """Функция сравнения списков.

    Функция считает, сколько различных чисел входит только в один из списков.
    """
    compare_difference = list_one ^ list_two
    return len(compare_difference)


def counting_different_words(text):
    """Функция подсчета слов.

    Функция определяет, сколько различных слов содержится в веденном тексте.
    """
    text_without_spaces = text.split(" ")
    set_text = set(text_without_spaces)
    return len(set_text)


def euclidean_algorithm(a, b):
    """Функция подсчета НОД.

    Функция вычисляет наибольший общий делитель двух чисел при помощи
    алгоритма Евклида.
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    else:
        return "Наибольший общий делитель: {}".format(a + b)
