import unittest
from unittest.mock import MagicMock, patch

from executor_base import ExecutorBase
from executor_human import ExecutorHuman
from executor_inode import ExecutorInode
from parser_base import ParserBase
from parser_human import ParserHuman
from parser_inode import ParserInode


class TestExecutor(unittest.TestCase):

    def setUp(self):
        self.executor_base = ExecutorBase(ParserBase())
        self.executor_human = ExecutorHuman(ParserHuman())
        self.executor_inode = ExecutorInode(ParserInode())

    @patch('subprocess.Popen')
    def test_execute_success(self, mock_popen):
        process_mock = MagicMock()
        attrs = {'communicate.return_value': ('output'.encode(), 'error'.encode()), 'returncode': 0}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        expected_result = {
            'status': 'Success',
            'error': 'None',
            'result': self.executor_base.parser.parse_output('output')
        }
        self.assertEqual(self.executor_base.execute(), expected_result)
        self.assertEqual(self.executor_human.execute(), expected_result)
        self.assertEqual(self.executor_inode.execute(), expected_result)

    @patch('subprocess.Popen')
    def test_execute_failure(self, mock_popen):
        process_mock = MagicMock()
        attrs = {'communicate.return_value': ('output'.encode(), 'error'.encode()), 'returncode': 1}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        expected_result = {
            'status': 'Failure',
            'error': 'error',
            'result': 'None'
        }
        self.assertEqual(self.executor_base.execute(), expected_result)
        self.assertEqual(self.executor_human.execute(), expected_result)
        self.assertEqual(self.executor_inode.execute(), expected_result)


if __name__ == "__main__":
    unittest.main()
