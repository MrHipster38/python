from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        num = func(*args)
        type_log = type(num)
        return {num: type_log}
    return wrapper

@type_logger
def some_func(num):
    result = num * 5
    return result

print(some_func.__name__, some_func(50))
