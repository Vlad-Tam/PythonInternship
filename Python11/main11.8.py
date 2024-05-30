class Dog:
    def __init__(self, height, weight, name, age, city='Minsk'):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__city = city

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, new_height: int):
        self.__height = new_height

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, new_weight: int):
        self.__height = new_weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: str):
        self.__age = new_age

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, new_city: str):
        self.__city = new_city

    def jump(self):
        print('JUMP!')

    def run(self):
        print('RUN!')

    def bark(self):
        print('BARK!')

    def __str__(self):
        return f'height={self.__height}, weight={self.__weight}, name={self.__name}, age={self.__age}, city={self.__city}'


if __name__ == "__main__":
    dog1 = Dog(12, 13, 'Sharik', 3, 'Moscow')
    print(dog1)
    print(dog1.height)
    dog1.height = 6
    print(dog1.height)
    dog1.city = 'Minsk'
    print(dog1)
