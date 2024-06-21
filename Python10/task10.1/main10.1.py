"""
Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""

if __name__ == "__main__":
    # task a
    with open('./file.txt', 'r') as file:
        print(file.readline())

    # task b
    with open('./file.txt', 'r') as file:
        for i in range(4):
            file.readline()
        print(file.readline())

    # task c
    with open('./file.txt', 'r') as file:
        for i in range(5):
            print(file.readline(), end='')
        print('')

    # task d
    s1 = 2
    s2 = 4
    with open('./file.txt', 'r') as file:
        for i in range(s1 - 1):
            file.readline()
        for i in range(s1 - 1, s2):
            print(file.readline(), end='')
        print('')

    # task e
    with open('./file.txt', 'r') as file:
        print(file.read())
