import sys
import csv
with open('bakery.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    try:
        start = int(sys.argv[1]) - 1
        try:
            end = int(sys.argv[2]) - 1
            for item in reader[start:end]:
                print(str(item)[2:-2])
        except IndexError:
            for item in reader[start:]:
                print(str(item)[2:-2])
    except IndexError:
        for item in reader:
            print(str(item)[2:-2])
