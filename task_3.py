
def logger(func):
    def wrapper(num):
        result = func(num)
        print(f'Имя функции - {func.__name__}, тип аргумента {num} - {type(num)}')
        return result
    return wrapper

@logger
def nums_cub(num):
    return num**3

print(nums_cub(3))