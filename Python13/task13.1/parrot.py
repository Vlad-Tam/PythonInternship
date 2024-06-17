from pet import Pet


class Parrot(Pet):
    def __init__(self, name: str, age: int, master: str, height: float, weight: float, species: str):
        super().__init__(name, age, master, height, weight)
        self.__species = species

    @property
    def species(self) -> str:
        return self.__species

    @species.setter
    def species(self, new_species: str) -> None:
        self.__species = new_species

    def change_height(self, value=0.05) -> None:
        self.height += float(value)

    def change_weight(self, value=0.05) -> None:
        self.weight += float(value)

    def fly(self):
        if self.weight > 0.1:
            print(f'Parrot cannot fly, current weight ({self.weight})')
        else:
            print(f'FLY! ({self.weight})')

    def jump(self, jump_height):
        if jump_height > 0.05:
            print('Parrots cannot jump so high')
        else:
            print(f'Parrot jump {jump_height} meters!')

    def voice(self):
        print('Parrot voice!')

    def __str__(self):
        return f'name={self.name}, age={self.age}, master={self.master}, height={self.height}, weight={self.weight}, ' \
               f'species={self.__species}'
