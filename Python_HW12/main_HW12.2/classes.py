import math
from abc import ABC, abstractmethod

class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, new_x: int) -> None:
        self.__x = new_x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, new_y: int) -> None:
        self.__y = new_y

    def __str__(self):
        return f'x={self.__x}, y={self.__y}'


class Figure(ABC):
    @abstractmethod
    def calculate_square(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, center: Point, radius: int):
        self.__center = center
        self.__radius = radius

    @property
    def center(self) -> Point:
        return self.__center

    @center.setter
    def center(self, new_center: Point) -> None:
        self.__center = new_center

    @property
    def radius(self) -> int:
        return self.__radius

    @radius.setter
    def radius(self, new_radius: int) -> None:
        self.__radius = new_radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_square(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    @property
    def point1(self) -> Point:
        return self.__point1

    @point1.setter
    def point1(self, new_point: Point) -> None:
        self.__point1 = new_point

    @property
    def point2(self) -> Point:
        return self.__point2

    @point2.setter
    def point2(self, new_point: Point) -> None:
        self.__point2 = new_point

    @property
    def point3(self) -> Point:
        return self.__point3

    @point3.setter
    def point3(self, new_point: Point) -> None:
        self.__point3 = new_point

    def calculate_perimeter(self):
        a = self.distance(self.__point1, self.__point2)
        b = self.distance(self.__point2, self.__point3)
        c = self.distance(self.__point3, self.__point1)
        return a + b + c

    def calculate_square(self):
        a = self.distance(self.__point1, self.__point2)
        b = self.distance(self.__point2, self.__point3)
        c = self.distance(self.__point3, self.__point1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    @staticmethod
    def distance(point1: Point, point2: Point):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


class Square(Figure):
    def __init__(self, point1: Point, point2: Point):
        self.__point1 = point1
        self.__point2 = point2

    @property
    def point1(self) -> Point:
        return self.__point1

    @point1.setter
    def point1(self, new_point: Point) -> None:
        self.__point1 = new_point

    @property
    def point2(self) -> Point:
        return self.__point2

    @point2.setter
    def point2(self, new_point: Point) -> None:
        self.__point2 = new_point

    def calculate_perimeter(self):
        a = self.distance(self.__point1, self.__point2)
        return 4 * a

    def calculate_square(self):
        a = self.distance(self.__point1, self.__point2)
        return a ** 2

    @staticmethod
    def distance(point1: Point, point2: Point):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
