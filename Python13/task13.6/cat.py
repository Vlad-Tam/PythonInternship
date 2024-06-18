from pet import Pet


class Cat(Pet):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def voice(self):
        print("CAT voice")
