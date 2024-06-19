"""
Просмотреть ваше задание, где вы реализовывали класс Car и подумать, где
стоит добавить выкидывание(raise) исключений(например, когда скорость
может стать меньше 0). В месте, где вы работаете с этим классом , добавьте
обработку этих исключений, используя конструкцию try
"""


from car import Car

if __name__ == "__main__":

    try:
        car = Car('', 'X5', 2020, -70)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        car = Car('BMW', '', 2020, -70)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        car = Car('BMW', 'X5', 2020, -70)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        car = Car('BMW', 'X5', -2020, 4)
    except ValueError as e:
        print(f"Error: {e}")

    car = Car('BMW', 'X5', 2020, 70)
    try:
        car.decrease_speed()
    except ValueError as e:
        print(f"Error: {e}")

    car.increase_speed()
    car.show_speed()
    car.decrease_speed()
    car.show_speed()
    car.stop()
    car.show_speed()
