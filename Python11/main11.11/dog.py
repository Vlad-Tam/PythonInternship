from pet import Pet


class Dog(Pet):
    def __init__(self, name: str, age: int, master: str, height: float, weight: float):
        super().__init__(name, age, master, height, weight)

    def bark(self):
        print('BARK!')
