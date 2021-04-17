tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Олег', 'Чебурек'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def my_gen():
    for idx in range(0, len(tutors) + 1):
        try:
            if idx > len(klasses) - 1:
                yield tutors[idx], None
            else:
                yield tutors[idx], klasses[idx]
        except IndexError:
            break

my_generator = my_gen()

print(my_gen())

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))




