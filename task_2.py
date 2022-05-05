from requests import get, utils

def currency_rates(value):
    value = value.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = (response.content.decode(encoding=encodings))
    content_split = content.split('<Valute ID=')

    total_score = 0
    flag = False

    for i in content_split:
        if value in i:
            total_score = float(i[(i.find('<Value>') + 7):(i.find('</Value>'))].replace(',', '.'))
            flag = True
        else:
            continue

    if flag == False:
        print(f'Информации по указанной валюте нет')
    else:
        print(f'{value} стоит {total_score:.02f} руб.')



if __name__ == 'main':
    currency_rates('usd')
    currency_rates('eur')
    print('Привет из задания 2')