from donkey import Donkey
from horse import Horse
from mule import Mule
from pet import Pet


def voice_animals(animals) -> None:
    for animal in animals:
        animal.voice()


if __name__ == "__main__":
    donkey = Donkey(12, "fgh", 1, 2)
    horse = Horse(2, "rty", 5, 6)
    mule = Mule(1, "cvb", 0, 0)
    try:
        pet = Pet(1, 'str', 12, 23)
    except TypeError:
        print("Error")
    donkey.voice()
    horse.voice()
    mule.voice()
    