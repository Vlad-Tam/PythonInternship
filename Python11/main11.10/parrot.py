from pet import Pet


class Parrot(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        print('FLY!')
