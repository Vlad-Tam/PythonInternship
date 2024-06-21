"""
Имеется текстовый файл. Переписать в другой файл все
его строки с заменой в них символа 0 на символ 1 и
наоборот.
"""

if __name__ == "__main__":
    with open('./file.txt', 'r') as file:
        with open('./res_file.txt', 'w') as res_file:
            while True:
                line = file.readline()
                if not line:
                    break
                result_str = ''
                for symbol in line:
                    if symbol == '1':
                        result_str += '0'
                    elif symbol == '0':
                        result_str += '1'
                    else:
                        result_str += symbol
                res_file.write(result_str)

