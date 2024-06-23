"""
Использовать результаты 10.8. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в task_10_09.py.
1) Создать функцию подсчета полной суммы всех товаров.
2) Создать функцию поиска самого дорогого товара.
3) Создать функцию самого дешевого товара.
4) Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""

from task10_8.csv_utils import *

if __name__ == "__main__":
    products_info = [['Apple', 12, 10, 'comment 1'],
                     ['Banana', 34, 5, 'comment 2'],
                     ['Strawberry', 5, 20, 'comment 3'],
                     ['Pineapple', 15, 2, 'comment 4']
                    ]
    write_csv('products.csv', products_info)
    print(read_csv('products.csv'))

    print(f"Total values is: {total_value('products.csv')}")
    print(f"Most expensive is: {find_most_expensive('products.csv')}")
    print(f"Cheapest is: {find_cheapest('products.csv')}")

    add_row('products.csv', ['Blackberry', 232, 12, 'comment 5'])
    del_row('products.csv', 3)
    print(read_csv('products.csv'))
    decrease_amount('products.csv', 6)
    print(read_csv('products.csv'))
