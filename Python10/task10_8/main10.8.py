"""
Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
записи(по позиции, по-умолчанию последнюю).
В файле task_10_08 (main10.8) импортировать функции. С помощью функций создать
файл с информацией о товарах(Имя товара, цена, количество,
комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""

from csv_utils import write_csv, read_csv, add_row, del_row

if __name__ == "__main__":
    products_info = [['name', 'price', 'count', 'comments'],
                     ['Apple', 12, 10, 'comment 1'],
                     ['Banana', 34, 5, 'comment 2'],
                     ['Strawberry', 5, 20, 'comment 3'],
                    ]
    write_csv('products.csv', products_info)
    print(read_csv('products.csv'))
    add_row('products.csv', ['Blackberry', 232, 2, 'comment 4'])
    del_row('products.csv', 3)
