def reform(list):
    for price in list:
        rub = int(price)
        penny = int((price - int(price)) * 100)
        print(f'{rub:02d} руб {penny:02d} коп', end=', ')
    print('')

prices = [46.7, 97.2, 34.84, 54, 779.52, 21.09, 13.3, 9.8, 55.06, 88.8]

reform(prices)
print(id(prices))
prices.sort()

reform(prices)
print(id(prices))

prices_sorted = sorted(prices, reverse = True)

reform(prices_sorted)
print(id(prices_sorted))

reform(prices_sorted[:5])



