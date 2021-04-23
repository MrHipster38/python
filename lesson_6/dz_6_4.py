database = {}

with open('users.csv', encoding='utf-8') as file_1, \
open('hobby.csv', encoding='utf-8') as file_2, \
open('users_hobby.txt', 'w+', encoding='utf-8') as f:
    for name, hobby in zip(file_1, file_2):
        f.write(f'{name.strip()}: {hobby}')





