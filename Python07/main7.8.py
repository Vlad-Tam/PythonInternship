from math import prod


def calculate_mean(*args, **kwargs):
    if kwargs.get('mean_type') == 'arithmetic':
        return sum(args) / len(args)
    elif kwargs.get('mean_type') == 'geometric':
        return prod(args) ** (1 / len(args))
    else:
        print("Invalid mean type, must be 'arithmetic' or 'geometric'")
        return


def arithmetic_mean(*args):
    return calculate_mean(mean_type='arithmetic', *args)


def geometric_mean(*args):
    return calculate_mean(mean_type='geometric', *args)


if __name__ == "__main__":
    print(arithmetic_mean(2, 4, 6, 8, 10))
    print(geometric_mean(2, 4, 6, 8, 10))
