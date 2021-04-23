import sys
database = {}
names = input('Введите имя файла с Именами: ')
hobbies = input('Введите имя файла с хобби: ')
user_hobby = input('Введите имя итогового файла: ')

with open(names, encoding='utf-8') as file_1, \
open(hobbies, encoding='utf-8') as file_2, \
open(user_hobby, 'w+', encoding='utf-8') as f:
    for name, hobby in zip(file_1, file_2):
        f.write(f'{name.strip()}: {hobby}')






