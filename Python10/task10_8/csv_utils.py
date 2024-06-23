import csv
from typing import List


def read_csv(filename: str) -> List:
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        return rows


def write_csv(filename: str, info: List[List]) -> None:
    with open(filename, 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(info)


def add_row(filename: str, row: List, pos: int = None) -> None:
    rows = read_csv(filename)
    if pos is None or pos >= len(rows):
        rows.append(row)
    else:
        rows.insert(pos, row)
    write_csv(filename, rows)


def del_row(filename: str, pos: int = None) -> None:
    rows = read_csv(filename)
    if pos is None:
        rows.pop()
    else:
        rows.pop(pos)
    write_csv(filename, rows)


def total_value(filename: str) -> float:
    total = 0
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            total += float(row[1]) * float(row[2])
    return total


def find_most_expensive(filename: str) -> List[str]:
    rows = read_csv(filename)
    most_expensive = rows[0]
    for row in rows:
        if float(row[1]) > float(most_expensive[1]):
            most_expensive = row
    return most_expensive


def find_cheapest(filename: str) -> List[str]:
    rows = read_csv(filename)
    cheapest = rows[0]
    for row in rows:
        if float(row[1]) < float(cheapest[1]):
            cheapest = row
    return cheapest


def decrease_amount(filename: str, n: int = 1) -> None:
    rows = read_csv(filename)
    try:
        for row in rows:
            row[2] = int(row[2]) - n
            if row[2] < 0:
                raise ValueError
    except ValueError:
        print('Values must be positive, changes are not save')
    else:
        write_csv(filename, rows)
