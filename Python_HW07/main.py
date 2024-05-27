def inches_to_cm(inches: float) -> float:
    return inches * 2.54


def cm_to_inches(cm: float) -> float:
    return cm / 2.54


def miles_to_km(miles: float) -> float:
    return miles * 1.609


def km_to_miles(km: float) -> float:
    return km / 1.609


def pounds_to_kg(pounds: float) -> float:
    return pounds * 0.454


def kg_to_pounds(kg: float) -> float:
    return kg / 0.454


def ounces_to_grams(ounces: float) -> float:
    return ounces * 28.35


def grams_to_ounces(grams: float) -> float:
    return grams / 28.35


def gallons_to_liters(gallons: float) -> float:
    return gallons * 3.785


def liters_to_gallons(liters: float) -> float:
    return liters / 3.785


def pints_to_liters(pints: float) -> float:
    return pints * 0.473


def liters_to_pints(liters: float) -> float:
    return liters / 0.473


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


def choice_function(choice: int, value: float):
    if choice == '1':
        print(f"{value} inches = {inches_to_cm(value)} cm")
    elif choice == '2':
        print(f"{value} cm = {cm_to_inches(value)} inches")
    elif choice == '3':
        print(f"{value} miles = {miles_to_km(value)} km")
    elif choice == '4':
        print(f"{value} km = {km_to_miles(value)} miles")
    elif choice == '5':
        print(f"{value} pounds = {pounds_to_kg(value)} kg")
    elif choice == '6':
        print(f"{value} kg = {kg_to_pounds(value)} pounds")
    elif choice == '7':
        print(f"{value} ounces = {ounces_to_grams(value)} g")
    elif choice == '8':
        print(f"{value} g = {grams_to_ounces(value)} ounces")
    elif choice == '9':
        print(f"{value} gallons = {gallons_to_liters(value)} l")
    elif choice == '10':
        print(f"{value} l = {liters_to_gallons(value)} gallons")
    elif choice == '11':
        print(f"{value} pints = {pints_to_liters(value)} l")
    elif choice == '12':
        print(f"{value} l = {liters_to_pints(value)} pints")
    else:
        print("Invalid choice. Please try again.")


def main():
    while True:
        output_menu()
        choice = input("Enter the number of the action: ")
        if choice == '0':
            break
        choice_function(choice, value=float(input("Enter the value: ")))


if __name__ == '__main__':
    main()

