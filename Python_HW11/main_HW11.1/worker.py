class Worker:
    def __init__(self, name: str, age: int, job_title: str):
        self.__name = name
        self.__age = age
        self.__job_title = job_title

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
    def age(self, new_age: int):
        self.__age = new_age

    @property
    def job_title(self) -> str:
        return self.__job_title

    @job_title.setter
    def job_title(self, new_job_title: str):
        self.__job_title = new_job_title

    def run(self):
        print(f'{self.name} is RUNNING')

    def sleep(self):
        print(f'{self.name} is SLEEPING')
