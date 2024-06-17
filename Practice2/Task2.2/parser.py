import re
from typing import Dict


class Parser:

    @staticmethod
    def get_fields_from_iperf(data, server_node, client_node) -> Dict:
        print(f'DATA:{data}')
        for line in data.strip().splitlines()[2:]:
            parts = re.split(r'\s{2,}', line.strip())
        print('PARTS=', parts[2], parts[3])
        return {
            'Server': {
                'ip': server_node.host,
                'name': server_node.username
            },
            'Client': {
                'ip': client_node.host,
                'name': client_node.username
            },
            'Interval': parts[2],
            'Transfer': parts[3],
            'Bandwidth': parts[4]
        }
