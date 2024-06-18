from wild_animal import WildAnimal


class Lion(WildAnimal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def voice(self):
        print("LION voice")
