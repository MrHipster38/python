def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num

odd_to_15 = odd_nums(15)

print(*odd_to_15)

max_num = int(input('Максимальное число: '))
odd_nums = (num for num in range(1, max_num + 1, 2))

print(*odd_nums)