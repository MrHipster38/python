try:
    duration = int(input('Введите количество секунд '))
    seconds = duration % 60
    minutes = duration % 3600 // 60
    hours= duration % 86400 // 3600
    days = duration // 86400

    if 0 < duration < 60:
        print(f'{seconds} сек')
    elif 0 < duration < 3600:
        print(f'{minutes} мин {seconds} сек')
    elif 0 < duration < 86400:
        print(f'{hours} час {minutes} мин {seconds} сек')
    elif duration >= 86400:
        print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
    else:
            print('Введите положительное число')
except ValueError:
    print('Необходимо ввести число целое число')
