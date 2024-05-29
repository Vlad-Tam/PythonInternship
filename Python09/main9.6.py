from datetime import datetime
from functools import reduce


def decorator(function):
    def wrapper(*args):
        start_time = datetime.now()
        function(*args)
        print(f'Executing time: {datetime.now() - start_time}')

    return wrapper


@decorator
def func(*args):
    for i in range(10000):
        print(reduce(lambda x, y: x * y, args))


if __name__ == "__main__":
    func(1, 3, 6, 2)
