from pet import Pet


class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        print('BARK!')
