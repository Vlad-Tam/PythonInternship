import json
import argparse

from executor_base import ExecutorBase
from executor_human import ExecutorHuman
from executor_inode import ExecutorInode
from parser_base import ParserBase
from parser_human import ParserHuman
from parser_inode import ParserInode


def main():
    parser = argparse.ArgumentParser(description='Disk Usage Utility')
    parser.add_argument('--human', action='store_true', help='Execute the "df -h" command')
    parser.add_argument('--inode', action='store_true', help='Execute the "df -i" command')
    args = parser.parse_args()
    if args.human and args.inode:
        print("Only one flag must be specified (--human or --inode)")
        return

    if args.human:
        df_executor = ExecutorHuman(ParserHuman())
    elif args.inode:
        df_executor = ExecutorInode(ParserInode())
    else:
        df_executor = ExecutorBase(ParserBase())

    result = df_executor.execute()
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
