def calculate_equation(a: int, b: int, c: int):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    elif d == 0:
        return (-b)/(2*a)
    else:
        return ((-b) + d**(1/2))/(2*a), ((-b) - d**(1/2))/(2*a)


def main():
    a = int(input('A*x^2 + B*x + C = 0\nInput A: '))
    b = int(input('Input B: '))
    c = int(input('Input C: '))
    print(calculate_equation(a, b, c))


if __name__ == "__main__":
    main()