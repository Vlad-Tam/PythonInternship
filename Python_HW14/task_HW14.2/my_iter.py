from typing import Any


class MyIter:
    def __init__(self, data: Any):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            if self.index % 2 == 0:
                res = self.data[self.index] ** 2
                self.index += 1
                return res
            else:
                self.index += 1
        raise StopIteration()
