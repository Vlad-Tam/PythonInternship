class Phone:
    def __init__(self, name: str, model: str, battery_life: int):
        self.__name = name
        self.__model = model
        self.__battery_life = battery_life

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, new_model: str):
        self.__model = new_model

    @property
    def battery_life(self) -> int:
        return self.__battery_life

    @battery_life.setter
    def battery_life(self, new_battery_life: int):
        self.__battery_life = new_battery_life

    def call(self):
        print(f'{self.name} is CALLING')

    def play_music(self):
        print(f'{self.name} is PLAYING MUSIC')
