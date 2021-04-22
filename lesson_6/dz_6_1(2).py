
my_list = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        my_tuple = (line_list[0], line_list[5][1:], line_list[6])
        my_list.append(my_tuple)



