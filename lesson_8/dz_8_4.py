from functools import wraps

def val_checker(callback):
    def my_decorator(func):
        @wraps(func)
        def wrapper(num):
           if callback(num):
               return func(num)
           else:
               raise ValueError(f'Wrong val {num}')
        return wrapper
    return my_decorator


@val_checker(lambda num: num > 0)
def calc(num):
    return num ** 3


a = calc(5)

print(a)
print(calc.__name__)


a = calc(-5)