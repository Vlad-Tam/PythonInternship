class Laptop:
    def __init__(self, name: str, brand: str, ram: int):
        self.__name = name
        self.__brand = brand
        self.__ram = ram

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, new_brand: str):
        self.__brand = new_brand

    @property
    def ram(self) -> int:
        return self.__ram

    @ram.setter
    def ram(self, new_ram: int):
        self.__ram = new_ram

    def work(self):
        print(f'{self.name} is WORKING')

    def charge(self):
        print(f'{self.name} is CHARGING')
