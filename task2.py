"""
Создайте декоратор, который хранит результаты вызова функции (за все время
вызовов, не только текущий запуск программы).
"""


def decorator(func):

    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        save_data = open("save_data.txt", "a")
        save_data.write(str(result_func) + "\n")
        save_data.close()

        return func(*args, **kwargs)
    return wrapper


@decorator
def func(x, y):
    return x + y


print(func(2, 4))
print(func(3, 4))
print(func(4, 6))
