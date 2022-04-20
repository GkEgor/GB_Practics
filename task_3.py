numbers = []

for i in range(1, 101):
    numbers.append(i)

for i in numbers:
    if (i == 1) or (i == 21) or (i == 31) or (i == 41) or (i == 51) or (i == 61) or (i == 71) or (i == 81) or (i == 91):
        print(i, 'процент')
    elif (i > 1 and i < 5) or (i > 21 and i < 25) or (i > 31 and i < 35) or (i > 41 and i < 45) or (i > 51 and i < 55) or (i > 61 and i < 65) or (i > 71 and i < 55) or (i > 81 and i < 85) or (i > 91 and i < 95):
        print(i, 'процента')
    elif (i > 4 and i < 21) or (i > 24 and i < 31) or (i > 34 and i < 41) or (i > 44 and i < 51) or (i > 54 and i < 61) or (i > 64 and i < 71) or (i > 74 and i < 81) or (i > 84 and i < 91) or (i > 94 and i <= 100):
        print(i, 'процентов')