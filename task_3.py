'''
без генератора
'''

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
while len(tutors) != len(klasses):
    tutors.append('None')
connect = zip(tutors, klasses)
list_connect = list(connect)
print(*list_connect)

'''
с генератором
'''
from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

some_gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))
print(*some_gen, sep='\n')