from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as user:
    some_list_user = user.read().splitlines()
with open('hobby.csv', 'r', encoding='utf-8') as hobby:
    some_list_hobby = hobby.read().splitlines()
if len(some_list_user) < len(some_list_hobby):
    print('Выход из скрипта с кодом "1"')
else:
    users_hobby = dict(zip_longest(some_list_user, some_list_hobby, fillvalue=None))
    print(users_hobby)
    with open('users_hobby.txt', 'w', encoding='utf-8') as file:
        json.dump(users_hobby, file, ensure_ascii=False)
