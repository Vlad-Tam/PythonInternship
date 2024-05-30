from cat import Cat
from dog import Dog
from parrot import Parrot

if __name__ == "__main__":
    cat = Cat("asd", 12, "fgh")
    dog = Dog("qwe", 2, "rty")
    parrot = Parrot("zxc", 1, "cvb")
    cat.meow()
    dog.bark()
    parrot.fly()
    print(cat, dog, parrot, sep=" | ")
