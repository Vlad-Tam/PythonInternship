from wild_animal import WildAnimal
from feline_interface import FelineInterface


class Lion(WildAnimal, FelineInterface):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def voice(self):
        print("LION voice")

    def purr(self):
        print('Lion is purring')

    def scratch(self):
        print('Lion is scratching')
