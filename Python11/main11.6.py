class Dog:
    def __init__(self, height, weight, name, age, master):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master

    def change_name(self, name):
        self.name = name

    def get_master(self):
        return self.__master

    def jump(self):
        print('JUMP!')

    def run(self):
        print('RUN!')

    def bark(self):
        print('BARK!')


if __name__ == "__main__":
    dog1 = Dog(12, 13, 'Sharik', 3, 'masterValue')
    print(dog1.get_master())

