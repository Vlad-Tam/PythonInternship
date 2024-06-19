import random
from time import sleep


def rand_generator():
    while True:
        yield random.randint(0, 1000)
        sleep(1)


if __name__ == "__main__":
    rand_gen = rand_generator()
    while True:
        try:
            print(next(rand_gen))
        except KeyboardInterrupt:
            print('Exit')
            break
            