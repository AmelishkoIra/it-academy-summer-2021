class TooManyErrors(Exception):
    """
    Декоратор, который вызывает задекорированную функцию пока она
    не выполнится без исключений (но не более n раз - параметр декоратора).
    Если превышено количество попыток, должно быть возбуждено исключение
    типа TooManyErrors.
    """
    pass

def parametric_decorator(n):
    def simple_decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            try:
                if count < n:
                    result = func(*args, **kwargs)
                    count += 1
                    return result
                else:
                    raise TooManyErrors("Many calls")
            except TooManyErrors as many:
                return many
            except:
                count = 0
                return "Error in the decorated function"

        return wrapper

    return simple_decorator

@parametric_decorator(3)
def division(a, b):
    return a / b

print(division(4, 9))
print(division(4, 4))
print(division(4, 6))
print(division(4, 1))
print(division(4, 0))