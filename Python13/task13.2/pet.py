import string
import random


class Pet:
    counter = 0

    def __init__(self, age: int, master: str, height: float, weight: float):
        self.__name = self.get_random_name()
        self.__age = age
        self.__master = master
        self.__height = height
        self.__weight = weight
        Pet.counter += 1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: str) -> None:
        self.__age = new_age

    @property
    def master(self) -> str:
        return self.__master

    @master.setter
    def master(self, new_master: str) -> None:
        self.__master = new_master

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, new_height: float) -> None:
        self.__height = new_height

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, new_weight: float) -> None:
        self.__weight = new_weight

    def change_height(self, value=0.2) -> None:
        self.__height += value

    def change_weight(self, value=0.2) -> None:
        self.__weight += value

    def jump(self, jump_height):
        print(f'Jump {jump_height} meters!')

    def run(self):
        print('RUN!')

    def sleep(self):
        print('SLEEP!')

    def voice(self):
        pass

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'name={self.__name}, age={self.__age}, master={self.__master}, height={self.__height}, weight={self.__weight}'

    @classmethod
    def get_counter(cls):
        return cls.counter

    @staticmethod
    def get_random_name():
        random_letter = random.choice(string.ascii_uppercase)
        random_number = random.randint(1, 100)
        return f"{random_letter}-{random_number}"
