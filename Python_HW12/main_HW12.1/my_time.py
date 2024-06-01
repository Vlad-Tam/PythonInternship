class MyTime:
    counter = 0

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.normalize_time()
        MyTime.counter += 1

    @classmethod
    def init_by_string(cls, time_str):
        hours, minutes, seconds = map(int, time_str.split('-'))
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
        self.normalize_time()

    @property
    def minutes(self) -> int:
        return self.__minutes

    @minutes.setter
    def minutes(self, new_minutes: int) -> None:
        self.__minutes = new_minutes
        self.normalize_time()

    @property
    def seconds(self) -> int:
        return self.__seconds

    @seconds.setter
    def seconds(self, new_seconds: int) -> None:
        self.__seconds = new_seconds
        self.normalize_time()

    def __eq__(self, other):
        return self.__hours == other.hours and self.__minutes == other.minutes and self.__seconds == other.seconds

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.__hours, self.__minutes, self.__seconds) < (other.hours, other.minutes, other.seconds)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

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

    def __mul__(self, other):
        result = MyTime()
        result_seconds = (self.__hours * 3600 + self.__minutes * 60 + self.__seconds) * other
        result.hours = result_seconds // 3600
        result_seconds -= result.hours * 3600
        result.minutes = result_seconds // 60
        result.seconds = result_seconds - result.minutes * 60
        return result

    def __str__(self):
        return f'{self.__hours}:{self.__minutes}:{self.__seconds}'

    def normalize_time(self):
        if self.__seconds >= 60:
            self.__minutes += self.__seconds // 60
            self.__seconds %= 60
        if self.__minutes >= 60:
            self.__hours += self.__minutes // 60
            self.__minutes %= 60

