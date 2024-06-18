from pet import Pet
from canine_interface import CanineInterface


class Dog(Pet, CanineInterface):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def voice(self):
        print("DOG voice")

    def bark(self):
        print('Dog is barking')

    def fetch(self):
        print('Dog is fetching')
