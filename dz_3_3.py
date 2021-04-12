def thesaurus(*args):
    dictionary = {}
    name_list = [*args]
    for name in name_list:
        if name[0] in dictionary.keys():
            dictionary[name[0]].append(name)
        else:
            temporary_dict = {name[0]: [name]}
            dictionary.update(temporary_dict)
    return dictionary


print(thesaurus('Иван', "Игорь", "Мария", "Костя", 'Вася', 'Ирина', 'Михаил'))
