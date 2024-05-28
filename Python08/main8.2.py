cars = [
    {"number": 123,
     "year": 2000
     },
    {"number": 13,
     "year": 2022
     },
    {"number": 1,
     "year": 2005
     },
    {"number": 33,
     "year": 2006
     }
]


def main():
    user_year = int(input("Input min year: "))
    new_cars = [car for car in cars if car.get("year") > user_year]
    print(new_cars)


if __name__ == "__main__":
    main()
