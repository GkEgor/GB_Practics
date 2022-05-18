n = int(input('Введите ограничение '))
not_even_num = (i for i in range(1, n + 1, 2))

print(type(not_even_num))
print(next(not_even_num))
print(next(not_even_num))
print(*not_even_num)
print(next(not_even_num))