import os
folder = 'some_data'
result = {}


def len_files(size, idx):
    files = [item
             for item in os.scandir(folder)
             if 10 ** (idx - 1) <= item.stat().st_size < size]
    print(f'выполняю цикл для размера {size}')
    return len(files)


for idx in range(0, 10):
    size = 10 ** idx
    if not len_files(size, idx):
        pass
    else:
        result[size] = len_files(size, idx)

print(result)