class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def jump(self):
        print('JUMP!')

    def run(self):
        print('RUN!')

    def bark(self):
        print('BARK!')


if __name__ == "__main__":
    dog1 = Dog(12, 13, 'Sharik', 3)
    dog1.run()
    dog1.jump()
    dog1.bark()
    print(dog1.height, dog1.weight, dog1.name, dog1.age, sep=', ')
    dog1.change_name('Mukhtar')
    print(dog1.height, dog1.weight, dog1.name, dog1.age, sep=', ')
