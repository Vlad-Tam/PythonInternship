import sys

if __name__ == "__main__":
    result = 0
    for arg in sys.argv:
        if arg.isdigit():
            result += int(arg)
    print(result)
