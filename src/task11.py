# число в правом столбце равно сумме "кругляшей",
# которые есть в цифрах числа, расположенного слева.
# Ваша задача написать программу, которая определяет,
# сколько кругляшей в числе.

n = input("Введите число ")
a = 0
for i in n:
    if i == "8":
        a = a + 2
    elif i == "0" or i == "6" or i == "9":
        a = a + 1
print(a)
