functions = {
    1: lambda inches: inches * 2.54,
    2: lambda cm: cm / 2.54,
    3: lambda miles: miles * 1.609,
    4: lambda km: km / 1.609,
    5: lambda pounds: pounds * 0.454,
    6: lambda kg: kg / 0.454,
    7: lambda ounces: ounces * 28.35,
    8: lambda grams: grams / 28.35,
    9: lambda gallons: gallons * 3.785,
    10: lambda liters: liters / 3.785,
    11: lambda pints: pints * 0.473,
    12: lambda liters: liters / 0.473
}


def output_menu():
    print("Select an action:")
    print("1. Inches to Centimeters")
    print("2. Centimeters to Inches")
    print("3. Miles to Kilometers")
    print("4. Kilometers to Miles")
    print("5. Pounds to Kilograms")
    print("6. Kilograms to Pounds")
    print("7. Ounces to Grams")
    print("8. Grams to Ounces")
    print("9. Gallons to Liters")
    print("10. Liters to Gallons")
    print("11. Pints to Liters")
    print("12. Liters to Pints")
    print("0. Exit")


def main():
    while True:
        output_menu()
        choice = int(input("Enter the number of the action: "))
        if choice == 0:
            break
        value = float(input("Enter the value: "))
        func = functions.get(choice)
        if func:
            print(func(value))


if __name__ == '__main__':
    main()
