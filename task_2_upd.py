'''
Задание 1а
реализация через цикл
'''
cub_numbers = []
new_cub_numbers = []

for i in range(1, 1000, 2):
    cub_numbers.append(i**3)
print('Стартовый список с кубами:', cub_numbers)

total = 0

for number in cub_numbers:
    double_number = number
    while double_number > 0:
        total += double_number % 10
        double_number = double_number // 10
    if total % 7 == 0:
        new_cub_numbers.append(number)
    total = 0
print()
print('Список кубов, сумма чисел которых делится на 7:',new_cub_numbers)
print()
print('Сумма:', sum(new_cub_numbers))

'''
Задание 1b
Реализация через цикл
'''
cub_numbers_seventeen = []
new_cub_numbers_seventeen = []

for i in range(1, 1000, 2):
    cub_numbers_seventeen.append(i**3)

cub_numbers_seventeen[:] = [i + 17 for i in cub_numbers_seventeen]
print('Стартовый список кубов + 17:', cub_numbers_seventeen)

total = 0

for number in cub_numbers_seventeen:
    double_number = number
    while double_number > 0:
        total += double_number % 10
        double_number = double_number // 10
    if total % 7 == 0:
        new_cub_numbers_seventeen.append(number)
    total = 0

print()
print('Список кубов, сумма чисел которых делится на 7:', new_cub_numbers_seventeen)
print()
print('Сумма:',sum(new_cub_numbers_seventeen))