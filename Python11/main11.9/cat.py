class Cat:
    def __init__(self, name, age, master):
        self.__name = name
        self.__age = age
        self.__master = master

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: str):
        self.__age = new_age

    @property
    def master(self) -> str:
        return self.__master

    @master.setter
    def master(self, new_master: str):
        self.__master = new_master

    def jump(self):
        print('JUMP!')

    def run(self):
        print('RUN!')

    def meow(self):
        print('MEOW!')

    def sleep(self):
        print('SLEEP!')

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'name={self.__name}, age={self.__age}, master={self.__master}'
