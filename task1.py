"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
runner. runner_one() – все фукнции вызываются по очереди,
runner_two(‘func_name’) – вызывается только функцию func_name,
runner_three(‘func’, ‘func1’...) - вызывает все переданные функции
"""

"""
Задача 2.1
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество S товара Посчитайте общую цену в рублях и
копейках за L товаров.
"""


def func_sum():
    print("Задача 2.1")
    m = int(input("цена за товар, руб.:"))
    n = int(input("цена за товар, коп.:"))
    p = int(m * 100 + n)
    w = int(input("куплено товара:"))
    h = (w * p) // 100
    t = (w * p) % 100
    print('цена за', w, 'ед.товара', h, "руб.", t, 'коп.')


"""
Задача 2.2
Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
"""


def long_word():
    print("Задача 2.2")
    words = input("Введите предложение: ")
    long_words = words.split()
    print(max(long_words, key=len))


"""
Задача 2.3
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
"""


def func():
    print("Задача 2.3")
    string = input("Введите строку: ")
    string_new = ""
    for i in range(len(string)):
        if string_new.find(string[i]) == -1 and string[i] != " ":
            string_new = string_new + string[i]
    return (string_new)


"""
Задача 2.4
Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.
"""


def letter_count():
    print("Задача 2.4")
    string = input("Введите строку: ")
    small_letters = ""
    big_letters = ""
    for i in range(len(string)):
        if string[i].islower() and string[i] != " ":
            small_letters = small_letters + string[i]
        elif string[i].isupper() and string[i] != " ":
            big_letters = big_letters + string[i]
    print(len(small_letters), " - строчные", len(big_letters), " - прописные ")


"""
Задача 2.5
Выведите n-ое число Фибоначчи.
"""


def fibonacci():
    print("Задача 2.5")
    n = int(input("Введите число: "))
    if n in (2, 3):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


"""
Задача 2.6
Определите, является ли число палиндромом.
"""


def palindrom():
    print("Задача 2.6")
    nomer_ = input("Введите число: ")
    nomer_new = nomer_[::-1]
    if nomer_ == nomer_new:
        print("Введенное число палиндром")
    else:
        print("Введенное число не палиндром")


"""
Задача 2.7
Даны: три стороны треугольника. Требуется: проверить, действительно ли это
стороны треугольника. Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""


def area_triangle():
    print("Задача 2.7")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
    if a + b > c and a + c > b and b + c > a:
        print("Площадь треугольника равно", s)
    else:
        print("Неверные данные")


"""
Задача 2.8
Дана строка и нужно найти ее первое слово
"""


def first_word():
    print("Задача 2.8")
    words = str(input("Введите предложение"))
    words_without_spaces = words.split()
    one_word = words_without_spaces[:1]
    print(one_word)


"""
Задача 2.9
В этой задаче, Вам нужно создать функцию проверки пароля. Условия проверки:
длина пароля должна быть больше 6. Входные данные: Строка.
"""


def password_verification():
    print("Задача 2.9")
    password = input("Введите пароль")
    n = len(password)
    if n <= 6:
        print("Пароль подходит по длине")
    else:
        print("Пароль слишком длинный")


"""
Задача 2.10
Требуется найти самую длинную непрерывную цепочку нулей в
последовательности нулей и единиц.нужно вывести искомую длину цепочки нулей.
"""


def continuous_chain():
    print("Задача 2.10")
    chain_10 = input("Введите строку из 0 и 1: ")
    chain_1 = chain_10.split("1")
    chain_0 = "0"
    for i in chain_1:
        if len(i) > len(chain_0):
            chain_0 = i
    print(len(chain_0))


"""
Задача 2.11
Число в правом столбце равно сумме "кругляшей", которые есть в цифрах числа,
расположенного слева. Ваша задача написать программу, которая определяет,
сколько кругляшей в числе.
"""


def round_numbers():
    print("Задача 2.11")
    number = input("Введите число ")
    round_number = 0
    for i in number:
        if i == "8":
            round_number = round_number + 2
        elif i == "0" or i == "6" or i == "9":
            round_number = round_number + 1
    print(round_number)


"""
Задача 2.12
Для заезда в оздоровительный лагерь организаторы решили заказать автобусы.
Известно, что в лагерь собираются поехать N детей и M взрослых. Каждый автобус
вмещает K человек. В каждом автобусе, в котором поедут дети, должно быть не
менее двух взрослых. Определите, удастся ли отправить в лагерь всех детей и
взрослых, и если да, то какое минимальное количество автобусов требуется для
этого заказать.
"""


def bus():
    import math
    print("Задача 2.12")
    children = int(input("число детей "))
    men = int(input("число взрослых "))
    bus_capacity = int(input("автобус вмещает человек "))
    number_bus = (children + men) / bus_capacity
    number_bus_ = math.ceil(number_bus)
    if men > 2 and men >= 2 * number_bus_:
        print("необходимо ", number_bus_, "автобуса")
    else:
        print("поездка не состоится")


"""
Задача 3.1
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz.
"""


def fizzbuzz():
    print("Задача 3.1")
    number = int(input("Введите число "))
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        print("FizzBuzz")
    elif int(number) % 3 == 0:
        print("Fizz")
    elif int(number) % 5 == 0:
        print("Buzz")
    else:
        print(number)


"""
Задача 3.2
Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd']. Используйте на предыдущий список slice
чтобы получить следующий: ['ab', 'ad', 'bc']. Используйте генератор списков
чтобы получить следующий ['1a', '2a', '3a', '4a']. Одной строкой удалите
элемент  '2a' из прошлого списка и напечатайте его. Скопируйте список и
добавьте в него элемент '2a' так чтобы в исходном списке этого элемента
не было.
"""


def gen_list():
    print("Задача 3.2")
    lst = "ab"
    lst1 = "bcd"
    lst2 = [i + j for i in lst for j in lst1]
    print(lst2)
    print(lst2[::2])
    lst3 = "1234"
    lst4 = [i + "a" for i in lst3]
    print(lst4)
    lst4.remove("2a")
    print(lst4)
    lst4.copy()
    lst4.append("2a")
    print(lst4)


"""
Задача 3.3
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж. Создайте кортеж
('a', 'b', 'c'), И сделайте из него список. Сделайте следующие присвоения одной
строкой a = 'a', b=2, c=’python’. Создайте кортеж из одного элемента, чтобы при
итерировании по этому элементы последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""


def list_and_tuple():
    list1 = ["a", "b", "c"]
    tpl1 = tuple(list1)
    print(tpl1, type(tpl1))
    tpl = ("a", "b", "c")
    lst = list(tpl)
    print(lst, type(lst))
    (a, b, c) = ("a", 2, "python")
    print(a, b, c)


"""
Задача 3.4
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Входные данные - строка из чисел, разделенная
пробелами. Выходные данные - количество пар.
"""


def number_of_pairs():
    print("Задача 3.4")
    number = input("Введите числа через пробел:")
    number_without_spaces = number.split(" ")
    ist_of_number = [int(s) for s in number_without_spaces]
    couples = 0
    for i in range(len(ist_of_number)):
        for j in range(i + 1, len(ist_of_number)):
            if ist_of_number[i] == ist_of_number[j]:
                couples += 1
    print(couples, " пары чисел")


"""
Задача 3.5
Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def meet_once_element():
    print("Задача 3.5")
    lst = [1, 2, 4, 5, 7, 7, 4]
    lst_new = ""
    for i in lst:
        if lst.count(i) <= 1:
            if str(i) not in lst_new:
                lst_new += str(i)
    print(lst_new)


"""
Задача 3.6
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
часть списка, не меняя их порядок, а все нули - в правую часть. Порядок
ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку. Распечатайте полученный список
"""


def separation_zero():
    print("Задача 3.6")
    lst = [1, 2, 4, 0, 5, 7, 7, 0, 4]
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    print(lst)


"""
Задача 4.1
Создайте словарь с помощью генератора словарей, так чтобы его ключами были
числа от 1 до 20, а значениями кубы этих чисел.
"""


def number_cube():
    print("Задача 4.1")
    cube_dictionary = {element: element ** 3 for element in range(1, 21)}
    print(cube_dictionary)


"""
Задача 4.2
Дан список стран и городов каждой страны. Затем даны названия городов. Для
каждого города укажите, в какой стране он находится. Входные данные: программа
получает на вход количество стран N. Далее идет N строк, каждая строка
начинается с названия страны, затем идут названия городов этой страны. В
следующей строке записано число M, далее идут M запросов — названия каких-то M
городов, перечисленных выше. Выходные данные Для каждого из запроса выведите
название страны, в котором находится данный город.
"""


def country_and_city():
    print("Задача 4.2")
    all = {}
    for i in range(int(input("Число стран: "))):
        all_ = input("Введите название страны и три ее города: ")
        country, *city = all_.split()
        all[country] = city
    cities = []
    for j in range(int(input("Число городов: "))):
        city = input("Введите название городов: ")
        cities.append(city)
        for key, value in all.items():
            if cities[j] in value:
                print(key)


"""
Задача 4.3
Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""


def compare_lists():
    print("Задача 4.3")
    list_one = {1, 3, 4, 67, 89, 23, 11}
    list_two = {2, 5, 4, 89, 25, 11, 13}
    compare = list_one & list_two
    print(len(compare))


"""
Задача 4.4
Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один
из этих списков.
"""


def compare_lists_difference():
    print("Задача 4.4")
    list_one = {1, 3, 4, 67, 89, 23, 11}
    list_two = {2, 5, 4, 89, 25, 11, 13}
    compare_difference = list_one ^ list_two
    print(len(compare_difference))


"""
Задача 4.5
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.
"""


def children_and_languages():
    print("Задача 4.5")
    children = int(input("Количество школьников: "))
    languages = []
    for i in range(children):
        if i <= children:
            languages_num = int(
                input(f"Количество языков школьника {i + 1}: "))
            for j in range(languages_num):
                if j <= languages_num:
                    languag = input("Введите языки: ")
                    languages.append(languag)
    set_languages = set(languages)
    languages_all = []
    for i in languages:
        if languages.count(i) == children:
            if i not in languages_all:
                languages_all.append(i)
    print("Кол-во языков, которые знают все школьники:", len(languages_all))
    print("Языки, которые знают все школьники: ", languages_all)
    print("Кол-во языков,которые знает хотя бы один школьник: ",
          len(set_languages))
    print("Языки, которые знает хотя бы один школьник: ", set_languages)


"""
Задача 4.6
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки. Определите, сколько различных слов
содержится в этом тексте.
"""


def counting_different_words():
    print("Задача 4.6")
    text = input("Text: ")
    text_without_spaces = text.split(" ")
    set_text = set(text_without_spaces)
    print(len(set_text))


"""
Задача 4.7
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
алгоритма Евклида.
"""


def euclidean_algorithm():
    a = int(input("Первое число "))
    b = int(input("Второе число "))
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    else:
        print("Наибольший общий делитель: ", a + b)


def runner_one():
    func_sum()
    long_word()
    func()
    letter_count()
    fibonacci()
    palindrom()
    area_triangle()
    first_word()
    password_verification()
    continuous_chain()
    round_numbers()
    bus()
    fizzbuzz()
    gen_list()
    list_and_tuple()
    number_of_pairs()
    meet_once_element()
    separation_zero()
    number_cube()
    country_and_city()
    compare_lists()
    compare_lists_difference()
    children_and_languages()
    counting_different_words()
    euclidean_algorithm()
    print("Функции выполнены")


runner_one()


def runner_two(func):
    func()
    print("Функция выполнена")


runner_two(continuous_chain)


def runner_three(*args, **kwargs):
    func_one()
    func_two()
    print("Функции выполнены")


func_one = euclidean_algorithm
func_two = counting_different_words


runner_three(func_one, func_two)
