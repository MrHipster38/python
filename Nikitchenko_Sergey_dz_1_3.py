
def percent(user_number):
    if 1 <= user_number <= 20:
        if user_number == 1:
            print(f'{user_number} процент')
        elif 2 <= user_number < 5:
            print(f'{user_number} процента')
        elif 5 <= user_number <= 20:
            print(f'{user_number} процентов')
    else:
        print('Необходимо ввести число от 1 до 20')

percent(1)
percent(3)
percent(6)