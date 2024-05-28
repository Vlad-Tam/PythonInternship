human = {
    "name": "Vlad",
    "age": 19,
    "height": 180
}


def main():
    new_dict = {value: key for key, value in human.items()}
    print(new_dict)


if __name__ == "__main__":
    main()
