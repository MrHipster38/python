some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
user_list = []

for item in some_list:
    if item.isdigit():
        num = '{:02d}'.format(int(item))
        user_list.extend(['"', num, '"'])
    elif item[0] == '+':
        num = '+{:02d}'.format(int(item))
        user_list.extend(['"', num, '"'])
    else:
        user_list.append(item)

print(' '.join(user_list))

