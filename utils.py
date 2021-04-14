import requests
import datetime


def currency_rates(valute):
    req = (requests.get('http://www.cbr.ru/scripts/XML_daily.asp')).text
    valute_list = req.split('</Valute>')
    """find date"""
    value_date = valute_list[0].split('Date=')[1][1:11]
    value_date_list = value_date.split('.')
    date = datetime.date(int(value_date_list[2]), int(value_date_list[1]), int(value_date_list[0]))
    """find value"""
    for i in valute_list:
        temporary_list = i.split('<CharCode>')
        if temporary_list[1][0:3] == valute:
            value = (temporary_list[1].split('<Value>'))[1][0:5]
            value_list = value.split(',')
            value_float = float(f'{value_list[0]}.{value_list[1]}')
            return f'{value_float}, {date}'
