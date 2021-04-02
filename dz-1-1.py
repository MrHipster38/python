duration = int(input('Введите количество секунд '))
s = duration % 60
m = duration % 3600 // 60
h = duration % 86400 // 3600
d = duration // 86400
if 0 < duration < 60:
    print(f'{s} сек')
elif duration < 3600:
    print(f'{m} мин {s} сек')
elif duration < 86400:
    print(f'{h} час {m} мин {s} сек')
elif duration >= 86400:
    print(f'{d} дн {h} час {m} мин {s} сек')
else:
    print('Введите положительное число')
