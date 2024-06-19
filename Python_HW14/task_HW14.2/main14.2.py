"""
Написать свой итератор(реализовать у него и метод __next__ и __iter__), чтобы
при обходе циклом он отдавал только элементы на четных индексах,
возведенные в квадрат.
"""

from my_iter import MyIter

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    iterator = MyIter(numbers)
    for item in iterator:
        print(item)
