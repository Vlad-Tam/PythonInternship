from pet import Pet


class Dog(Pet):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def voice(self):
        print("DOG voice")
