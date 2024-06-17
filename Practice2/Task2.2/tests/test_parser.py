import unittest
from parser import Parser
from sshpass import SSHPass


class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_base_parse_output(self):
        info_str = '------------------------------------------------------------\n' \
                   'Server listening on TCP port 5001\n' \
                   'TCP window size: 85.3 KByte (default)\n' \
                   '------------------------------------------------------------\n' \
                   '[  4] local 192.168.1.100 port 5001 connected to 192.168.1.101 port 48704' \
                   '[ ID]  Interval     Transfer      Bandwidth\n' \
                   '[  3]  0.0-10.0 sec  1.25 GBytes  1.07 Gbits/sec\n'
        server = SSHPass('192.168.1.1', 'username1', '123')
        client = SSHPass('192.168.1.2', 'username2', '123')

        expected_result = {
            'Server': {
                'ip': '192.168.1.1',
                'name': 'username1'
            },
            'Client': {
                'ip': '192.168.1.2',
                'name': 'username2'
            },
            'Interval': '0.0-10.0 sec',
            'Transfer': '1.25 GBytes',
            'Bandwidth': '1.07 Gbits/sec'
        }
        self.assertEqual(self.parser.get_fields_from_iperf(info_str, server, client), expected_result)
