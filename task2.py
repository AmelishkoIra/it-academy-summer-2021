"""
Создайте декоратор, который хранит результаты вызова функции (за все время
вызовов, не только текущий запуск программы).
"""


def decorator(func):
    
    count = []
    def wrapper(*args, **kwargs):
        nonlocal count
        count.append(func(*args, **kwargs))
        print("Все результаты вызова функции", count)
        return func(*args, **kwargs)
    return wrapper


@decorator
def func(x, y):
    return x + y


print(func(2, 4))
print(func(3, 4))
print(func(4, 6))
