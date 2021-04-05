def sum_num_list(number):
    sum = 0
    num_list = list(str(number))
    for numb in num_list:
        sum += int(numb)
    return sum

my_list = []
for num in range(0, 1000):
    if num % 2:
        my_list.append(num ** 3)

summary = 0
for num in my_list:
    if not sum_num_list(num) % 7:
        summary += num
print(summary)

for idx in range(0, len(my_list)):
    my_list[idx] += 17
    

summary = 0
for num in my_list:
    if not sum_num_list(num) % 7:
        summary += num
print(summary)


