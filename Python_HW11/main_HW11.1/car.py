class Car:
    def __init__(self, name: str, color: str, max_velocity: int):
        self.__name = name
        self.__color = color
        self.__max_velocity = max_velocity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, new_color: str):
        self.__color = new_color

    @property
    def max_velocity(self) -> int:
        return self.max_velocity

    @max_velocity.setter
    def max_velocity(self, new_max_velocity: int):
        self.__max_velocity = new_max_velocity

    def beep(self):
        print(f'BEEP by {self.name}')

    def ride(self):
        print(f'RIDING by {self.name}')
