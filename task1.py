# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

lst = [el for el in range(101)]
str_ = []
for i in lst:
    if int(i) % 3 == 0 and int(i) % 5 == 0:
        str_.append("FizzBuzz")
    elif int(i) % 3 == 0:
        str_.append("Fizz")
    elif int(i) % 5 == 0:
        str_.append("Buzz")
    else:
        str_.append(i)
print(str_)
