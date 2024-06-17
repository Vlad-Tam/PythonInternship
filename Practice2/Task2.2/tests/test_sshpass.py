import unittest
from unittest.mock import patch, mock_open

from sshpass import SSHPass


class TestSSHPass(unittest.TestCase):
    def setUp(self):
        self.host = "test_host"
        self.username = "test_user"
        self.password = "test_password"
        self.subcommand = "ssh"

    def test_constructor(self):
        ssh_pass = SSHPass(self.host, self.username, self.password, self.subcommand)
        self.assertEqual(ssh_pass.host, self.host)
        self.assertEqual(ssh_pass.username, self.username)
        self.assertEqual(ssh_pass.password, self.password)
        self.assertEqual(ssh_pass.subcommand, self.subcommand)

    def test_run_command_with_password(self):
        ssh_pass = SSHPass(self.host, self.username, self.password, self.subcommand)
        mock_output = {'stdout': 'test output', 'stderr': 'test error', 'return code': 0}
        with patch('subprocess.Popen') as mock_popen:
            mock_popen.return_value.communicate.return_value = (mock_output['stdout'].encode(),
                                                                mock_output['stderr'].encode())
            mock_popen.return_value.returncode = mock_output['return code']
            result = ssh_pass.run_command('test_command')
            self.assertEqual(result, mock_output)

    def test_run_command_with_password_file(self):
        ssh_pass = SSHPass(self.host, self.username, None, self.subcommand)
        mock_output = {'stdout': 'test output', 'stderr': 'test error', 'return code': 0}
        with patch('subprocess.Popen') as mock_popen:
            mock_popen.return_value.communicate.return_value = (mock_output['stdout'].encode(),
                                                                mock_output['stderr'].encode())
            mock_popen.return_value.returncode = mock_output['return code']
            with patch('builtins.open', mock_open(read_data=self.password)):
                result = ssh_pass.run_command('test_command')
                self.assertEqual(result, mock_output)

    def test_run_command_error(self):
        ssh_pass = SSHPass(self.host, self.username, self.password, self.subcommand)
        mock_output = {'stdout': 'test error', 'stderr': 'test error', 'return code': 1}
        with patch('subprocess.Popen') as mock_popen:
            mock_popen.return_value.communicate.return_value = (mock_output['stdout'].encode(),
                                                                mock_output['stderr'].encode())
            mock_popen.return_value.returncode = mock_output['return code']
            result = ssh_pass.run_command('test_command')
            self.assertEqual(result, mock_output)

    def test_check_subcommand(self):
        ssh_pass = SSHPass(self.host, self.username, self.password, 'ssh')
        self.assertEqual(ssh_pass.check_subcommand(), ' ')

        ssh_pass.subcommand = 'scp'
        self.assertEqual(ssh_pass.check_subcommand(), ':')
