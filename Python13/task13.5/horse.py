from pet import Pet


class Horse(Pet):
    def __init__(self, age: int, master: str, height: float, weight: float):
        super().__init__(age, master, height, weight)

    def voice(self):
        print('HORSE voice!')
