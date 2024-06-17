import unittest
from unittest.mock import patch
from iperf import IperfCommand


class TestIperf(unittest.TestCase):
    def setUp(self):
        self.ip1 = "192.168.1.100"
        self.name1 = "user1"
        self.password1 = "pass1"
        self.ip2 = "192.168.1.101"
        self.name2 = "user2"
        self.password2 = "pass2"
        self.iperf_command = IperfCommand(self.ip1, self.name1, self.password1, self.ip2, self.name2, self.password2)

    def test_execute(self):
        mock_server_output = {'stdout': 'Server output', 'stderr': '', 'return code': 0}
        mock_client_output = {'stdout': 'Client output', 'stderr': '', 'return code': 0}
        mock_parser_output = {'parsed_output': 'Parsed output'}

        with patch.object(self.iperf_command, 'run_server', return_value=mock_server_output), \
             patch.object(self.iperf_command, 'wait_for_server', return_value=123), \
             patch.object(self.iperf_command, 'run_client', return_value=mock_client_output), \
             patch.object(self.iperf_command, 'kill_server_process', return_value={'stdout': '', 'stderr': '',
                                                                                   'return code': 0}), \
             patch.object(self.iperf_command.parser, 'get_fields_from_iperf',
                          return_value=mock_parser_output['parsed_output']):
            result = self.iperf_command.execute()
            self.assertEqual(result, {'stdout': mock_parser_output['parsed_output'], 'stderr': '', 'return code': 0})

    def test_run_server(self):
        mock_server_output = {'stdout': 'Server output', 'stderr': '', 'return code': 0}
        with patch.object(self.iperf_command.node1, 'run_command', return_value=mock_server_output):
            result = self.iperf_command.run_server()
            self.assertEqual(result, mock_server_output)

    def test_run_client(self):
        mock_client_output = {'stdout': 'Client output', 'stderr': '', 'return code': 0}
        with patch.object(self.iperf_command.node2, 'run_command', return_value=mock_client_output):
            result = self.iperf_command.run_client()
            self.assertEqual(result, mock_client_output)

    def test_wait_for_server(self):
        mock_ps_output = {'stdout': 'PID\n123', 'stderr': '', 'return code': 0}
        with patch.object(self.iperf_command.node1, 'run_command', return_value=mock_ps_output):
            result = self.iperf_command.wait_for_server()
            self.assertEqual(result, '123')

    def test_wait_for_server_timeout(self):
        mock_ps_output = {'stdout': 'PID\n', 'stderr': '', 'return code': 0}
        with patch.object(self.iperf_command.node1, 'run_command', return_value=mock_ps_output):
            result = self.iperf_command.wait_for_server()
            self.assertEqual(result, -1)

    def test_kill_server_process(self):
        mock_kill_output = {'stdout': '', 'stderr': '', 'return code': 0}
        with patch.object(self.iperf_command.node1, 'run_command', return_value=mock_kill_output):
            result = self.iperf_command.kill_server_process(123)
            self.assertEqual(result, mock_kill_output)
