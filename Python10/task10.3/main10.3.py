"""
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""

if __name__ == "__main__":
    with open('./file.txt', 'a') as file:
        for i in range(3):
            file.write(input(f'Input new ({i + 1}) string: ') + '\n')
