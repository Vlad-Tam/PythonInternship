class Pet:
    def __init__(self, name: str, age: int, master: str, height: float, weight: float):
        self.__name = name
        self.__age = age
        self.__master = master
        self.__height = height
        self.__weight = weight

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
    def name(self, new_height: float) -> None:
        self.__name = new_height

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def name(self, new_weight: float) -> None:
        self.__name = new_weight

    def change_height(self, value=0.2) -> None:
        self.__height += value

    def change_weight(self, value=0.2) -> None:
        self.__weight += value

    def jump(self):
        print('JUMP!')

    def run(self):
        print('RUN!')

    def sleep(self):
        print('SLEEP!')

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'name={self.__name}, age={self.__age}, master={self.__master}, height={self.__height}, weight={self.__weight}'
