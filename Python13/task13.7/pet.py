from animal import Animal
from abc import ABC, abstractmethod


class Pet(Animal, ABC):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @abstractmethod
    def voice(self):
        pass
