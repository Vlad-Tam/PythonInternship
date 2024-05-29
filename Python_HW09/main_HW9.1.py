from datetime import datetime
from functools import reduce


def decorator(function):
    def wrapper(*args):
        print(f'Arguments: {args}')
        start_time = datetime.now()
        function(*args)
        print(f'Executing time: {datetime.now() - start_time}')
    return wrapper


@decorator
def func(*args):
    res = 0
    for i in range(10000):  # to increase executing time
        res += reduce(lambda x, y: x * y, args)
    print(res)


if __name__ == "__main__":
    func(1, 3, 6, 2)
