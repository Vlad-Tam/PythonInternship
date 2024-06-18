from cat import Cat
from dog import Dog
from lion import Lion
from wolf import Wolf
from feline_interface import FelineInterface
from canine_interface import CanineInterface


def main() -> None:
    animals = [Cat('Vlad', 12), Dog('Vlad', 13), Lion('Vlad', 14), Wolf('Vlad', 15)]
    for animal in animals:
        print(animal)
        animal.voice()
        if issubclass(animal.__class__, FelineInterface):
            animal.purr()
            animal.scratch()
        if issubclass(animal.__class__, CanineInterface):
            animal.fetch()
            animal.bark()


if __name__ == "__main__":
    main()
