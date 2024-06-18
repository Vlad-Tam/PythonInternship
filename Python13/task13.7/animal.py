from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def voice(self):
        pass

    def __str__(self):
        return f'name={self.name}, age={self.age}'
