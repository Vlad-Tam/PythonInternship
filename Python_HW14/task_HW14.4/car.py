class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int = 0):
        self.validate_brand(brand)
        self.validate_model(model)
        self.validate_year(year)
        self.validate_speed(speed)

        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, new_brand: str):
        self.validate_brand(new_brand)
        self.__brand = new_brand

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, new_model: str):
        self.validate_model(new_model)
        self.__model = new_model

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, new_year: int):
        self.validate_year(new_year)
        self.__year = new_year

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, new_speed: int):
        self.validate_speed(new_speed)
        self.__speed = new_speed

    """
    In the old version the speed could be negative, 
    now an exception is thrown if the speed is negative
    and the previous value remains
    """

    def increase_speed(self):
        if self.__speed >= 0:
            temp_speed = self.__speed + 5
        else:
            temp_speed = self.__speed - 5
        self.validate_speed(temp_speed)
        self.__speed = temp_speed

    def decrease_speed(self):
        if self.__speed >= 0:
            temp_speed = self.__speed - 5
        else:
            temp_speed = self.__speed + 5
        self.validate_speed(temp_speed)
        self.__speed = temp_speed

    def stop(self):
        self.__speed = 0

    def show_speed(self):
        print(f'The speed is {self.__speed} km/h')

    # In any case will throw exception
    # def turn_around(self):
    #     temp_speed = self.__speed * -1
    #     self.validate_speed(temp_speed)
    #     self.__speed = temp_speed

    def validate_brand(self, brand: str) -> None:
        if len(brand.strip()) == 0 or not isinstance(brand, str):
            raise ValueError('Brand must be not empty')

    def validate_model(self, model: str) -> None:
        if len(model.strip()) == 0 or not isinstance(model, str):
            raise ValueError('Model must be not empty')

    def validate_year(self, year: int) -> None:
        if not isinstance(year, int) or year <= 0:
            raise ValueError('Year must be positive')

    def validate_speed(self, speed: int) -> None:
        if not isinstance(speed, int) or speed <= 0:
            raise ValueError('Speed must not be negative')
