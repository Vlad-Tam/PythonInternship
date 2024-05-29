check_starts_with = lambda s, symbol: s.startswith(symbol)


if __name__ == "__main__":
    string = input('Input string: ')
    char = input('Input symbol: ')
    print(check_starts_with(string, char))