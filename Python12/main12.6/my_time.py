class MyTime:
    counter = 0
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        MyTime.counter += 1
        print('New object created')

    @classmethod
    def init_by_string(cls, time_str):
        hours, minutes, seconds = time_str.split('-')
        return cls(hours, minutes, seconds)

    @classmethod
    def init_by_object(cls, time_obj):
        return cls(time_obj.hours, time_obj.minutes, time_obj.seconds)

    @property
    def hours(self) -> int:
        return self.__hours

    @hours.setter
    def hours(self, new_hours: int) -> None:
        self.__hours = new_hours

    @property
    def minutes(self) -> int:
        return self.__minutes

    @minutes.setter
    def minutes(self, new_minutes: int) -> None:
        self.__minutes = new_minutes

    @property
    def seconds(self) -> int:
        return self.__seconds

    @seconds.setter
    def seconds(self, new_seconds: int) -> None:
        self.__seconds = new_seconds

    def __eq__(self, other):
        return self.__seconds == other.seconds and self.__minutes == other.minutes and self.__hours == other.hours

    def __ne__(self, other):
        return not (self.__seconds == other.seconds and self.__minutes == other.minutes and self.__hours == other.hours)

    def __add__(self, other):
        result = MyTime()
        result_seconds = (self.__hours * 3600 + self.__minutes * 60 + self.__seconds) + \
                         (other.hours * 3600 + other.minutes * 60 + other.seconds)
        result.hours = result_seconds // 3600
        result_seconds -= result.hours * 3600
        result.minutes = result_seconds // 60
        result.seconds = result_seconds - result.minutes * 60
        return result

    def __sub__(self, other):
        result = MyTime()
        result_seconds = (self.__hours * 3600 + self.__minutes * 60 + self.__seconds) - \
                         (other.hours * 3600 + other.minutes * 60 + other.seconds)
        result.hours = result_seconds // 3600
        result_seconds -= result.hours * 3600
        result.minutes = result_seconds // 60
        result.seconds = result_seconds - result.minutes * 60
        return result

    def __str__(self):
        return f'{self.__hours}-{self.__minutes}-{self.__seconds}'
