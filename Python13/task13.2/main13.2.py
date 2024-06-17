from cat import Cat
from dog import Dog
from parrot import Parrot
from pet import Pet


if __name__ == "__main__":
    print(f'Counter={Pet.get_counter()}')
    cat = Cat(12, "fgh", 1, 2)
    dog = Dog(2, "rty", 5, 6)
    parrot = Parrot(1, "cvb", 0, 0, 'White')
    print(f'Counter={Pet.get_counter()}')
    print(cat.name)
    print(dog.name)
    print(parrot.name)
    