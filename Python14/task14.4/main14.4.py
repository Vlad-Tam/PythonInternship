import argparse
import csv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first_name', required=True, type=str)
    parser.add_argument('-ln', '--last_name', required=True, type=str)
    parser.add_argument('-a', '--age', required=True, type=int)
    args = parser.parse_args()

    human = [args.first_name, args.last_name, args.age]
    with open('people.csv', 'a', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(human)
    print('Success')
