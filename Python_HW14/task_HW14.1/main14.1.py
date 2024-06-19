"""
Написать свой класс MyOpen, объекты которого должны поддерживать
протокол контекстного менеджера. Он должен работать аналогично with
open(‘file.txt’, ‘w+’) as f. Т.е вы можете применять его следующим образом:
with MyOpen(file.txt’, ‘w+’) as f:
"""

from my_open import MyOpen

if __name__ == "__main__":
    with MyOpen('./test.txt', 'r') as f:
        for line in f:
            print(line)
