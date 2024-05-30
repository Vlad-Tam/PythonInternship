class Dog:
    def __init__(self, height, weight, name, age, master, city='Minsk'):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master
        self.__city = city

    def change_name(self, name):
        self.name = name

    def get_master(self):
        return self.__master

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def jump(self):
        print('JUMP!')

    def run(self):
        print('RUN!')

    def bark(self):
        print('BARK!')


if __name__ == "__main__":
    dog1 = Dog(12, 13, 'Sharik', 3, 'masterValue')
    print(dog1.get_city())
    dog1.set_city('Moscow')
    print(dog1.get_city())
