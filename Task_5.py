prices = [57.80, 46.51, 97, 49.25, 56.4, 47.45, 58, 61.99, 97.40, 25.48, 84.65, 99.30]
new_prices = []

for price in prices:
    a = int(price)
    b = (price % int(price)) * 100
    b = int(round(b, 2))
    total_price = f'{a} руб. {b:02.0f} коп.'
    new_prices.append(total_price)
    total_price = None
print(new_prices)
print(f'id моего списка на начальном этапе: {id(new_prices)}')
new_prices.sort()
print(new_prices)
print(f'id моего списка после сортирования по возрастанию: {id(new_prices)}')

prices = [57.80, 46.51, 97, 49.25, 56.4, 47.45, 58, 61.99, 97.40, 25.48, 84.65, 99.30]
new_prices = []

for price in prices:
    a = int(price)
    b = (price % int(price)) * 100
    b = int(round(b, 2))
    total_price = f'{a} руб. {b:02.0f} коп.'
    new_prices.append(total_price)
    total_price = None

print(new_prices)
print(f'id моего списка на начальном этапе: {id(new_prices)}')
new_prices.sort(reverse= True)
print(new_prices)
print(f'id моего списка после сортирования по убыванию: {id(new_prices)}')
print(f'Пять самых дорогих товаров: {new_prices[:5]}')


