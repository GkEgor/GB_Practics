import re


def parse_mail(mail):
    re_mail = re.match(r'.+\@\w+\.\w+', mail)
    if re_mail:
        mail_split = re_mail.group().split('@')
        username = mail_split[0]
        domain = mail_split[1]
        return {'username': username, 'domain': domain}
    else:
        raise ValueError(f'Введенен некорректный email ({mail})')


print(parse_mail('rws19.93@mail.ru'))
print(parse_mail('rws19.93mail.ru'))


