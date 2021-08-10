"""Функции из Homework2 для тестирования"""


import math


def func_sum(m, n, w):
    """
    Расчет общей цены в рублях и копейках за w товаров.
    m - цена за товар, руб.; n - цена за товар, коп.; w - куплено товара.
    """
    p = int(m * 100 + n)
    h = (w * p) // 100
    t = (w * p) % 100
    return h, t


def long_word(words):
    """
    Нахождение самого длинного слова в введенном предложении.
    """
    list_words = words.split()
    long_words = max(list_words, key=len)
    return long_words


def del_space(string):
    """
    Функция удаляет из строки повторяющиеся символы и все пробелы.
    """
    string_new = ""
    string = string.lower()
    for i in range(len(string)):
        if string_new.find(string[i]) == -1 and string[i] != " ":
            string_new = string_new + string[i]
    return string_new


def letter_count(string):
    """
    Считает количество строчных (маленьких) и прописных (больших) букв в
    введенной строке.
    """
    small_letters = ""
    big_letters = ""
    for i in range(len(string)):
        if string[i].islower() and string[i] != " ":
            small_letters = small_letters + string[i]
        elif string[i].isupper() and string[i] != " ":
            big_letters = big_letters + string[i]
    num_small_letters = len(small_letters)
    num_big_letters = len(big_letters)
    return num_small_letters, num_big_letters


def fibonacci(n):

    """Выводит n-ое число Фибоначчи"""

    if n < 2:
        return str(n - 1)
    else:
        i = 2
        f = [0, 1, 1]
        while i < n:
            f[2] = f[0] + f[1]
            f[0] = f[1]
            f[1] = f[2]
            i += 1
        return str(f[2])


def palindrom(nomer):

    """Определяет, является ли число палиндромом."""
    nomer_ = str(nomer)
    nomer_new = nomer_[::-1]
    if nomer_ == nomer_new:
        return True
    else:
        return False


def area_triangle(a, b, c):
    """
    Проверка существования треугольника и выичсление его площади.
    a, b, c - три стороны треугольника, s - площадь треугольника.
    """
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
    if a + b > c and a + c > b and b + c > a:
        return ("Площадь треугольника равно {}".format(s))
    else:
        return ("Неверные данные")


def first_word(words):
    """ Находит первое слово в строке"""

    words_without_spaces = words.split()
    one_word = words_without_spaces[:1]
    return one_word


def password_verification(password):
    """
    Функция проверки пароля. Условия проверки: длина пароля должна быть
    больше 6. Входные данные: Строка.
    """
    n = len(password)
    if n > 6:
        return ("Пароль подходит по длине")
    else:
        return ("Пароль не подходит")


def continuous_chain(chain_10):
    """
    Находит самую длинную непрерывную цепочку нулей в последовательности нулей
    и единиц. Выводит длину искомой цепочки нулей.
    """
    chain_1 = chain_10.split("1")
    chain_0 = "0"
    for i in chain_1:
        if len(i) > len(chain_0):
            chain_0 = i
    return len(chain_0)


def round_numbers(number):
    """ Функция определяет, сколько кругляшей в числе """
    round_number = 0
    for i in number:
        if i == "8":
            round_number = round_number + 2
        elif i == "0" or i == "6" or i == "9":
            round_number = round_number + 1
    return round_number


def bus(children, men, bus_capacity):
    """
    Определет, удастся ли отправить в лагерь всех детей и взрослых, и если да,
    то указывает какое минимальное количество автобусов требуется для этого
    заказать.
    children - количество детей,
    men - количество взрослых,
    bus_capacity - вместимость автобуса,
    number_bus - необходимое количество автобусов
    """
    number_bus = math.ceil((children + men) / bus_capacity)
    if men > 2 and men >= 2 * number_bus:
        return "необходимо {} автобусa".format(number_bus)
    else:
        return "поездка не состоится"
