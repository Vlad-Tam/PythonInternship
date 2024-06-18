from pet import Pet
from feline_interface import FelineInterface


class Cat(Pet, FelineInterface):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def voice(self):
        print("CAT voice")

    def purr(self):
        print('Cat is purring')

    def scratch(self):
        print('Cat is scratching')
