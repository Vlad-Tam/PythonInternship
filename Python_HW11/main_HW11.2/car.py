class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int = 0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, new_brand: str):
        self.__brand = new_brand

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, new_model: str):
        self.__model = new_model

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, new_year: int):
        self.__year = new_year

    @property
    def speed(self) -> int:
        return self.__speed

    def increase_speed(self):
        if self.__speed >= 0:
            self.__speed += 5
        else:
            self.__speed -= 5

    def decrease_speed(self):
        if self.__speed >= 0:
            self.__speed -= 5
        else:
            self.__speed += 5

    def stop(self):
        self.__speed = 0

    def show_speed(self):
        print(f'The speed is {self.__speed} km/h')

    def turn_around(self):
        self.__speed *= -1