import math
from string import ascii_letters

"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
runner. runner() – все фукнции вызываются по очереди,
runner(‘func_name’) – вызывается только функцию func_name,
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

"""
Задача 2.1
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество S товара Посчитайте общую цену в рублях и
копейках за L товаров.
m - цена за товар, руб.; n - цена за товар, коп.; w - куплено товара.
"""

def func_sum(m=1, n=1, w=1):
    print("Задача 2.1")
    p = int(m * 100 + n)
    h = (w * p) // 100
    t = (w * p) % 100
    print('цена за', w, 'ед.товара', h, "руб.", t, 'коп.')


"""
Задача 2.2
Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
"""


def long_word(words="Hello worlds"):
    print("Задача 2.2")
    long_words = words.split()
    print(max(long_words, key=len))


"""
Задача 2.3
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
"""


def del_space(string="Hello world"):
    print("Задача 2.3")
    string_new = ""
    for i in range(len(string)):
        if string_new.find(string[i]) == -1 and string[i] != " ":
            string_new = string_new + string[i]
    print(string_new)


"""
Задача 2.4
Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.
"""

def letter_count(string="Hello world"):
    print("Задача 2.4")
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

def fibonacci(n=1):
    print("Задача 2.5")
    if n < 2:
        print("Число Фибоначчи:", str(n - 1))
    else:
        i = 2
        f = [0, 1, 1]
        while i < n:
            f[2] = f[0] + f[1]
            f[0] = f[1]
            f[1] = f[2]
            i += 1
        print("Число Фибоначчи:", str(f[2]))


"""
Задача 2.6 
Определите, является ли число палиндромом.
"""

def palindrom(nomer=1):
    print("Задача 2.6")
    nomer_ = str(nomer)
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


def area_triangle(a=1, b=1, c=1):
    print("Задача 2.7")
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


def first_word(words="Hello world"):
    print("Задача 2.8")
    words_without_spaces = words.split()
    one_word = words_without_spaces[:1]
    print(one_word)


"""
Задача 2.9
В этой задаче, Вам нужно создать функцию проверки пароля. Условия проверки:
длина пароля должна быть больше 6. Входные данные: Строка.
"""


def password_verification(password="1234"):
    print("Задача 2.9")
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


def continuous_chain(chain_10="000110"):
    print("Задача 2.10")
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


def round_numbers(number="146"):
    print("Задача 2.11")
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


def bus(children=2, men=3, bus_capacity=7):

    print("Задача 2.12")
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


def fizzbuzz(number=1):
    print("Задача 3.1")
    #number = int(input("Введите число "))
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


def gen_list(lst="ab", lst1="bcd", lst3="1234"):
    print("Задача 3.2")
    lst2 = [i + j for i in lst for j in lst1]
    print(lst2)
    print(lst2[::2])
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


def list_and_tuple(list1=["a", "b", "c"], tpl=("a", "b", "c")):
    tpl1 = tuple(list1)
    print(tpl1, type(tpl1))
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


def number_of_pairs(number="12 33 12"):
    print("Задача 3.4")
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


def meet_once_element(lst=[1, 2, 4, 5, 7, 7, 4]):
    print("Задача 3.5")
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


def separation_zero(lst=[1, 2, 4, 0, 5, 7, 7, 0, 4]):
    print("Задача 3.6")
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

def country_and_city(list_country_and_cities=None, city_search=None):

    print("Задача 4.2")

    if city_search is None:
        city_search = ["Moscow", "Odessa"]

    if list_country_and_cities is None:
        list_country_and_cities = ["Russia Moscow Petersburg Novgorod Kaluga",
                                   "Ukraine Kiev, Lviv, Odessa"]
    dict_country_and_cities = {}
    for str_country_and_cities in list_country_and_cities:
        list_cities = []
        str_country_and_cities = str_country_and_cities.split()
        for cities_of_the_country in str_country_and_cities[1:]:
            list_cities.append(cities_of_the_country)
        dict_country_and_cities[str_country_and_cities[0]] = list_cities
    countries = ""
    for i in city_search:
        for country, cities_of_the_country in dict_country_and_cities.items():
            if i in cities_of_the_country:
                countries += country + "\n"
    print(countries)


"""
Задача 4.3
Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""


def compare_lists(list_one={4, 67, 89, 23, 11},list_two={5, 4, 89, 25, 11}):
    print("Задача 4.3")
    compare = list_one & list_two
    print(len(compare))


"""
Задача 4.4
Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один
из этих списков.
"""


def compare_lists_difference(list_one={4, 67, 89, 23, 11},
                             list_two={5, 4, 89, 25, 11}):
    print("Задача 4.4")
    compare_difference = list_one ^ list_two
    print(len(compare_difference))


"""
Задача 4.5
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.
Дано: Три школьника. Языки первого: en, bel, rus. Языки второго: en, bel, gen.
Языки третьего: en, bel, rus, ger.
"""


def children_and_languages(languages_child_one={"en", "bel", "rus"},
                           languages_child_two={"en", "bel", "ger"},
                           languages_child_three={"en", "bel", "ger", "rus"},
                           *args, **kwargs):
    print("Задача 4.5")
    languages_all = languages_child_one & languages_child_two\
                    & languages_child_three
    set_languages = languages_child_one | languages_child_two |\
                    languages_child_three
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


def counting_different_words(text="Hello world"):
    print("Задача 4.6")
    #text = input("Text: ")
    text_without_spaces = text.split(" ")
    set_text = set(text_without_spaces)
    print(len(set_text))



"""
Задача 4.7
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
алгоритма Евклида.
"""


def euclidean_algorithm(a=1, b=2):
    #a = int(input("Первое число "))
    #b = int(input("Второе число "))
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    else:
        print("Наибольший общий делитель: ", a + b)
        

names_in_module = dir()
list_names_of_functions = []
for name in names_in_module:
    if name.startswith("__") and name.endswith("__"):
        continue
    elif name == "ascii_letters":
        continue
    elif name == "math":
        continue
    else:
        list_names_of_functions.append(name)


def runner(*args):
    if not args:
        for func_name in list_names_of_functions:
            start = globals()[func_name]
            start()
    for func_name in args:
        start = globals()[func_name]
        start()


runner()
runner("bus")
runner("func_sum", "del_space")
