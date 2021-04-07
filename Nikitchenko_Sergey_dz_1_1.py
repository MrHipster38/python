duration = int(input('Введите количество секунд: '))
seconds = duration % 60
minutes = (duration % 3600) // 60
hours = duration // 3600
days = duration // 86400

if duration < 60:
    print(f'{seconds} секунд')
elif 60 <= duration < 3600:
    print(f'{minutes} минут {seconds} секунд')
elif 3600 <= duration < 86400:
    print(f'{hours}')
