a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
if a + b > c and a + c > b and b + c > a:
    print("Площадь треугольника равно", s)
else:
    print("Неверные данные")
