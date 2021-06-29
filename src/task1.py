# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

list_numbers = []
for i in range(1, 101):
    if int(i) % 3 == 0 and int(i) % 5 == 0:
        list_numbers.append("FizzBuzz")
    elif int(i) % 3 == 0:
        list_numbers.append("Fizz")
    elif int(i) % 5 == 0:
        list_numbers.append("Buzz")
    else:
        list_numbers.append(i)
print(list_numbers)
