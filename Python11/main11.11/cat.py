from pet import Pet


class Cat(Pet):
    def __init__(self, name: str, age: int, master: str, height: float, weight: float):
        super().__init__(name, age, master, height, weight)

    def meow(self):
        print('MEOW!')
