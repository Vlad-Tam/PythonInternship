from pet import Pet


class Cat(Pet):
    def __init__(self, name: str, age: int, master: str, height: float, weight: float):
        super().__init__(name, age, master, height, weight)

    def voice(self):
        print('MEOW!')

    def jump(self, jump_height):
        if jump_height > 2:
            print('Cats cannot jump so high')
        else:
            print(f'Cat jump {jump_height} meters!')
