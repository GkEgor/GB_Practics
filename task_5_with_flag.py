'''
Номер 5 с флагом, правом выбора длины и повторов
'''


from random import *

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(length, delete):
    i = 0
    while i < length:
        a_ind, b_ind, c_ind = randrange(len(nouns)), randrange(len(adverbs)), randrange(len(adjectives))
        print(f'"{nouns[a_ind]} {adverbs[b_ind]} {adjectives[c_ind]}"',end=' ')
        if delete == 'yes':
            del nouns[a_ind]
            del adverbs[b_ind]
            del adjectives[c_ind]
        i += 1
user_answe_1 = int(input('Введите количество шуток, но не больше 5 '))
user_answer_2 = input('Если хотите убрать повторения слов введите "yes" ')

get_jokes(user_answe_1, user_answer_2)