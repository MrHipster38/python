src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = []
tmp = set()

for num in src:
    try:
        if num not in tmp:
            result.append(num)
        else:
            result.remove(num)
    except ValueError:
        pass
    tmp.add(num)

print(result)
