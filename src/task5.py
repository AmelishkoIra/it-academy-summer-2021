# Выведите n-ое число Фибоначчи, используя только временные
# переменные, циклические операторы и условные операторы.
n1 = 0
n2 = 1

n = int(input("Введите порядковый номер числа в ряду: "))

i = 0
while i < n - 2:
    m = n1 + n2
    n1 = n2
    n2 = m
    i = i + 1

print("Искомое число:", n2)
