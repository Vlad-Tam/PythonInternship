from car import Car

if __name__ == "__main__":
    car = Car('BMW', 'X5', 2020, 70)
    car.show_speed()
    car.increase_speed()
    car.increase_speed()
    car.show_speed()
    car.turn_around()
    car.show_speed()
    car.decrease_speed()
    car.show_speed()
    car.stop()
    car.show_speed()
