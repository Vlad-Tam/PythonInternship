"""
Написать генератор, который будет принимать на вход имя файла и
генерировать построчно(т.е yield каждой строки).
"""


def my_gen(filename: str):
    try:
        with open(filename, 'r', newline='') as file:
            for line in file:
                yield line
    except FileNotFoundError:
        print('File is not found')


if __name__ == "__main__":
    file_generator = my_gen('./test.txt')
    for file_line in file_generator:
        print(file_line, end='')
