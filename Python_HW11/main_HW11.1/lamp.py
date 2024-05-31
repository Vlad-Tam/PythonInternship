class Lamp:
    def __init__(self, name: str, color: str, brightness: int):
        self.__name = name
        self.__color = color
        self.__brightness = brightness

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, new_color: str):
        self.__color = new_color

    @property
    def brightness(self) -> int:
        return self.__brightness

    @brightness.setter
    def brightness(self, new_brightness: int):
        self.__brightness = new_brightness

    def blink(self):
        print(f'{self.name} is BLINKING')

    def shine(self):
        print(f'{self.name} is SHINING')
