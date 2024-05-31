from car import Car
from lamp import Lamp
from laptop import Laptop
from phone import Phone
from worker import Worker

if __name__ == "__main__":
    car = Car('Mercedes', 'Blue', 122)
    car.beep()
    lamp = Lamp('Xiaomi', 'Black', 1232)
    lamp.blink()
    laptop = Laptop('Magicbook', 'Huawei', 16)
    laptop.charge()
    phone = Phone('Xiaomi', 'Redmi Note 10', 4500)
    phone.call()
    worker = Worker('Vlad', 20, 'Programmer')
    worker.sleep()