'''
Номер 1
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
    for k, v in words.items():
        if user_answer == k:
            print(v)
    return None

tranlate(words)