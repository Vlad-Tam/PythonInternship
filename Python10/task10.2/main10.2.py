"""
Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры
"""

if __name__ == "__main__":
    with open('./file.txt', 'w') as file:
        for i in range(6):
            file.write(input(f'Input {i + 1} string: ') + '\n')
