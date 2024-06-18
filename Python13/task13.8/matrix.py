import random

class Matrix:
    def __init__(self, n=5, m=5, a=0, b=10):
        self.n = n
        self.m = m
        self.data = [[random.randint(a, b) for _ in range(m)] for _ in range(n)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def find_max(self):
        return max(max(row) for row in self.data)

    def find_min(self):
        return min(min(row) for row in self.data)

    def sum_all(self):
        return sum(sum(row) for row in self.data)
