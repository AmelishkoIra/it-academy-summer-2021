# Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
# списке этого элемента не было.

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
