some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(some_list))
idx = 0
while idx < len(some_list):
    if some_list[idx].isdigit():
        some_list[idx] = f'{int(some_list[idx]):02d}'
        some_list.insert(idx,  '"')
        some_list.insert(idx + 2,  '"')
        idx += 3

    elif some_list[idx][0] == '+':
        some_list[idx] = f'+{int(some_list[idx]):02d}'
        some_list.insert(idx, '"')
        some_list.insert(idx + 2, '"')
        idx += 3
    else:
        idx += 1
print(' '.join(some_list))
print(id(some_list))