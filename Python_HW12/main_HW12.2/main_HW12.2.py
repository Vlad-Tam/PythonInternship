from classes import Point, Circle, Triangle, Square

if __name__ == "__main__":
    figures = [
        Circle(Point(0, 0), 5),
        Triangle(Point(0, 0), Point(3, 0), Point(0, 4)),
        Square(Point(-1, 0), Point(4, 0))
    ]

    for figure in figures:
        print(figure.calculate_square())
