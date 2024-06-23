"""
Имеются два текстовых файла с одинаковым числом
строк. Выяснить, совпадают ли их строки. Если нет, то
получить номер первой строки, в которой эти файлы
отличаются друг от друга.
"""

if __name__ == "__main__":
    with open('./first.txt', 'r') as first_file:
        with open('./second.txt', 'r') as second_file:
            string_num = 1
            while True:
                first_line = first_file.readline()
                second_line = second_file.readline()
                if not first_line or not second_line:
                    break
                if first_line != second_line:
                    print(f'First different string number: {string_num}')
                    break
                string_num += 1
