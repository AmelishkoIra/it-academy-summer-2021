# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

input_num = input("Введите числа через пробел:")
num = input_num.split(" ")
ist_of_number = [int(s) for s in num]
couples = 0
for i in range(len(ist_of_number)):
    for j in range(i + 1, len(ist_of_number)):
        if ist_of_number[i] == ist_of_number[j]:
            couples += 1
print(couples, " пары чисел")
