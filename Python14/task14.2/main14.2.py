import random
from time import sleep


def rand_generator(a: int, b: int, n: int):
    while True:
        yield random.randint(a, b)
        a += n
        b += n
        sleep(1)


if __name__ == "__main__":
    rand_gen = rand_generator(1, 10, 10)
    while True:
        try:
            print(next(rand_gen))
        except KeyboardInterrupt:
            print('Exit')
            break
