try:
    duration = int(input('Введите количество секунд '))
    seconds = duration % 60
    minutes = duration % 3600 // 60
    hours= duration % 86400 // 3600
    days = duration % 2629746 // 86400
    months = duration % 31556952 // 2629746
    years = duration // 31556952
    if 0 < duration < 60:
        print(f'{seconds} сек')
    elif 0 < duration < 3600:
        print(f'{minutes} мин {seconds} сек')
    elif 0 < duration < 86400:
        print(f'{hours} час {minutes} мин {seconds} сек')
    elif 0 < duration < 2629746:
        print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
    elif 0 < duration < 31556952:
        print(f'{months} мес {days} дн {hours} час {minutes} мин {seconds} сек')
    elif duration >= 31556952:
        print(f'{years} лет {months} мес {days} дн {hours} час {minutes} мин {seconds} сек')
    else:
            print('Введите положительное число')
except ValueError:
    print('Необходимо ввести число целое число')
