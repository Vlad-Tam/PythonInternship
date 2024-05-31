from typing import List

from cat import Cat
from dog import Dog
from parrot import Parrot


def voice_animals(animals) -> None:
    for animal in animals:
        animal.voice()


if __name__ == "__main__":
    cat = Cat("asd", 12, "fgh", 1, 2)
    dog = Dog("qwe", 2, "rty", 5, 6)
    parrot = Parrot("zxc", 1, "cvb", 0, 0, 'White')
    voice_animals([cat, dog, parrot])
    