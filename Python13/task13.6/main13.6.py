from cat import Cat
from dog import Dog
from lion import Lion
from wolf import Wolf


def main() -> None:
    animals = [Cat('Vlad', 12), Dog('Vlad', 13), Lion('Vlad', 14), Wolf('Vlad', 15)]
    for animal in animals:
        print(animal)
        animal.voice()


if __name__ == "__main__":
    main()
