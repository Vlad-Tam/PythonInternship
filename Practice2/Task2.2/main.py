import argparse
from argparse import Namespace
from iperf import IperfCommand


def get_args() -> Namespace:
    parser = argparse.ArgumentParser(description='Iperf Utility')
    parser.add_argument('ip1', type=str, help='IP address 1 (server)')
    parser.add_argument('ip2', type=str, help='IP address 2 (client)')
    parser.add_argument('name1', type=str, help='Name 1 (server)')
    parser.add_argument('name2', type=str, help='Name 2 (client)')
    parser.add_argument('pass1', type=str, help='Password 1 (server)')
    parser.add_argument('pass2', type=str, help='Password 2 (client)')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    iperf_executor = IperfCommand(args.ip1, args.name1, args.pass1, args.ip2, args.name2, args.pass2)
    print(f'Bandwidth is: {iperf_executor.execute()}')
