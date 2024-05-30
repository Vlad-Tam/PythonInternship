from pet import Pet


class Cat(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        print('MEOW!')
