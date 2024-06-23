"""
Имеется текстовый файл. Все четные строки этого файла
записать во второй файл, а нечетные — в третий файл.
Порядок следования строк сохраняется.
"""

if __name__ == "__main__":
    with open('./file.txt', 'r') as file:
        with open('./even.txt', 'w') as even_file:
            with open('./odd.txt', 'w') as odd_file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                    odd_file.write(line)
                    line = file.readline()
                    if not line:
                        break
                    even_file.write(line)
