# Даны два списка чисел. Посчитайте, сколько
# различных чисел входит только в один из этих списков.

list_one = {1, 3, 4, 67, 89, 23, 11}
list_two = {2, 5, 4, 89, 25, 11, 13}
list_three = list_one ^ list_two
print(len(list_three))
