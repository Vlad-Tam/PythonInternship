from functools import reduce

if __name__ == "__main__":
    numbers = [3, 7, 9, 10, 5, 18, 6, 2, 7]
    multiples_of_3 = list(filter(lambda z: z % 3 == 0, numbers))
    print(multiples_of_3)
    result = reduce(lambda x, y: x * y, multiples_of_3)
    print(result)
