from pet import Pet


class Dog(Pet):
    def __init__(self, name: str, age: int, master: str, height: float, weight: float):
        super().__init__(name, age, master, height, weight)

    def bark(self):
        print('BARK!')

    def jump(self, jump_height):
        if jump_height > 0.5:
            print('Dogs cannot jump so high')
        else:
            print(f'Dog jump {jump_height} meters!')
