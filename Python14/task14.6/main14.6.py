import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', '--directory_name', required=True, type=str)
    parser.add_argument('-f', '--file_name', required=True, type=str)
    args = parser.parse_args()
    try:
        os.mkdir(f'./{args.directory_name}')
    except FileExistsError:
        pass
    finally:
        with open(f'./{args.directory_name}/{args.file_name}', 'w'):
            pass
        print('Created')
