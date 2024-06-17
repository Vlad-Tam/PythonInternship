from donkey import Donkey
from horse import Horse
from mule import Mule


def voice_animals(animals) -> None:
    for animal in animals:
        animal.voice()


if __name__ == "__main__":
    donkey = Donkey(12, "fgh", 1, 2)
    horse = Horse(2, "rty", 5, 6)
    mule = Mule(1, "cvb", 0, 0)
    donkey.voice()
    horse.voice()
    mule.voice()
    