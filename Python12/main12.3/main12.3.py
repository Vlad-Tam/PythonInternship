from cat import Cat
from dog import Dog
from parrot import Parrot

if __name__ == "__main__":
    cat = Cat("asd", 12, "fgh", 1, 2)
    dog = Dog("qwe", 2, "rty", 5, 6)
    parrot = Parrot("zxc", 1, "cvb", 0, 0, 'White')
    print(parrot)
    parrot.species = 'Blue'
    print(parrot)
