'''
Код не рабочий, показал сторону в которую думал.

Решил переборать список, по проверке принт выдает спикски, все ОК.
Но я не понимаю, почему принт не выдает мне нужный список, если я ставлю условие, что если (name) - аргумент функции == v (значению), он мне вообще ничего не печатает.

В целом, я думаю, что решение идет куда-то в это сторону, но что-то дойти не могу
'''


some_name = {
    'И': ['Иван', 'Илья'],
    'М': ['Мария'],
    'П': ['Петр']
}

print(some_name)

def thesaurus(name):
    for k, v in some_name.items():
        print(k, v)
        if v == name:
            print(k, v)
        else:
            continue


thesaurus('Иван')