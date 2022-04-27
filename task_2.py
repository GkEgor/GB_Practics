'''
Номер 1 upd. Приведение к нужному регистру через проверку
'''

words = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def tranlate(words):
    user_answer = input('Введите слово на английском от 0 до 10 ')
    if user_answer != user_answer.title():
        user_answer = user_answer.title()
    for k, v in words.items():
        if k != k.title() and v != v.title():
            k = k.title()
            v = v.title()
        if user_answer == k:
            print(v)
    return None

tranlate(words)