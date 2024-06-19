import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', '--directory_name', required=True, type=str)
    args = parser.parse_args()
    try:
        os.mkdir(f'./{args.directory_name}')
    except FileExistsError:
        print('Directory already exists')
    else:
        print('Created')
