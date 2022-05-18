'''
без генератора
'''

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = []
for i in src:
    if src.count(i) == 1:
        unique_src.append(i)
print(unique_src)

'''
с генератором
'''

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_scr = (i for i in src if src.count(i) == 1)
print(list(unique_scr))


