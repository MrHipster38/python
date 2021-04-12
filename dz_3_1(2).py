

def num_translate_adv(num):
    dictionary = {'one': 'один',
                  'two': 'два',
                  'three': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eight': 'восемь',
                  'nine': 'девять',
                  'ten': 'десять'}
    if num[0].upper() == num[0]:
        num = num.lower()
        return dictionary[num].title()
    elif num in dictionary.keys():
        num = num.lower()
        return dictionary[num]


print(num_translate_adv('Two'))
print(num_translate_adv('four'))
print(num_translate_adv('eleven'))
