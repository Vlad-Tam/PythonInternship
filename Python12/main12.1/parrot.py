from pet import Pet


class Parrot(Pet):

    def __init__(self, name: str, age: int, master: str, height: float, weight: float):
        super().__init__(name, age, master, height, weight)

    def fly(self):
        if self.weight > 0.1:
            print(f'Parrot cannot fly, current weight ({self.weight})')
        else:
            print(f'FLY! ({self.weight})')

    def change_height(self, value=0.05) -> None:
        self.height += float(value)

    def change_weight(self, value=0.05) -> None:
        self.weight += float(value)
