from functools import wraps


def checker(l_func):
    def checker_wraps(func):
        @wraps(func)
        def wrapper(num):
            if l_func(num):
                result = func(num)
            else:
                raise ValueError(f'Введенено некорректное число ({num})')
            return result
        return wrapper
    return checker_wraps

@checker(lambda num: num > 0)
def nums_cub(num):
    return num**3

print(nums_cub(3))
print(nums_cub(-3))