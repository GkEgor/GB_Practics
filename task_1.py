duration = int(input('Введите число для преобразования во время '))

if duration < 60:
    seconds = duration
    print(seconds, 'секунд(ы)')
elif duration >= 60 and duration < 3600:
    seconds = duration % 60
    minutes = (duration // 60) % 3600
    print(minutes, 'минут(ы)', seconds, 'секунд(ы)')
elif duration >= 3600 and duration < 86400:
    hours = (duration // 3600) % 24
    minutes = (duration // 60) % 60
    seconds = duration % 60
    print(hours, 'час(ов)', minutes, 'минут(ы)', seconds, 'секунд(ы)')
elif duration >= 86400:
    days = (duration // 86400) % 365
    hours = (duration // 3600) % 24
    minutes = (duration // 60) % 60
    seconds = duration % 60
    print(days, 'дней', hours, 'час(ов)', minutes, 'минут(ы)', seconds, 'секунд(ы)')