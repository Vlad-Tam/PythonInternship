from wild_animal import WildAnimal
from canine_interface import CanineInterface


class Wolf(WildAnimal, CanineInterface):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def voice(self):
        print("WOLF voice")

    def bark(self):
        print('Wolf is barking')

    def fetch(self):
        print('Wolf is fetching')
