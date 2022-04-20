'''
Задание 2а
'''

cub_numbers = []
new_cub_numbers = []

for i in range(1, 1000, 2):
    cub_numbers.append(i**3)
print('Стартовый список с кубами:', cub_numbers)


for i in cub_numbers:
    a = i // 100000000
    b = (i % 100000000) // 10000000
    c = (i % 10000000) // 1000000
    d = (i % 1000000) // 100000
    e = (i % 100000) // 10000
    f = (i % 10000) // 1000
    g = (i % 1000) // 100
    h = (i % 100) // 10
    j = i % 10
    s = a + b + c + d + e + f + g + h + j
    if s % 7 == 0:
        new_cub_numbers.append(i)

print()
print('Список кубов, сумма чисел которых делится на 7:', new_cub_numbers)
print()
print('Сумма:', sum(new_cub_numbers))

'''
Задание 2b
'''
cub_numbers_seventeen = []
new_cub_numbers_seventeen = []

for i in range(1, 1000, 2):
    cub_numbers_seventeen.append(i**3)

cub_numbers_seventeen[:] = [i + 17 for i in cub_numbers_seventeen]
print('Стартовый список кубов + 17:', cub_numbers_seventeen)

for i in cub_numbers_seventeen:
    a = i // 100000000
    b = (i % 100000000) // 10000000
    c = (i % 10000000) // 1000000
    d = (i % 1000000) // 100000
    e = (i % 100000) // 10000
    f = (i % 10000) // 1000
    g = (i % 1000) // 100
    h = (i % 100) // 10
    j = i % 10
    s = a + b + c + d + e + f + g + h + j
    if s % 7 == 0:
        new_cub_numbers_seventeen.append(i)
print()
print('Список кубов, сумма чисел которых делится на 7:', new_cub_numbers_seventeen)
print()
print('Сумма:',sum(new_cub_numbers_seventeen))







