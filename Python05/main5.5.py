def main():
    surnames = ["Петров", "Петрова", "Иванов", "Иванова", "Сидоров", "Сидорова", "Павлова", "Попова"]
    result_surnames = [surname for surname in surnames if surname.startswith("П") and surname.endswith("а")]
    for surname in result_surnames:
        print(surname)


if __name__ == '__main__':
    main()
