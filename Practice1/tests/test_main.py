import unittest
from executor_base import ExecutorBase
from executor_human import ExecutorHuman
from executor_inode import ExecutorInode
from unittest.mock import MagicMock, patch
import main


class TestMain(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args')
    def test_main_human(self, mock_args):
        mock_args.return_value = MagicMock(human=True, inode=False)
        with patch.object(ExecutorHuman, 'execute', return_value='test') as mock_execute:
            main.main()
            mock_execute.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args')
    def test_main_inode(self, mock_args):
        mock_args.return_value = MagicMock(human=False, inode=True)
        with patch.object(ExecutorInode, 'execute', return_value='test') as mock_execute:
            main.main()
            mock_execute.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args')
    def test_main_base(self, mock_args):
        mock_args.return_value = MagicMock(human=False, inode=False)
        with patch.object(ExecutorBase, 'execute', return_value='test') as mock_execute:
            main.main()
            mock_execute.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args')
    def test_main_both_flags(self, mock_args):
        mock_args.return_value = MagicMock(human=True, inode=True)
        with patch('builtins.print') as mock_print:
            main.main()
            mock_print.assert_called_once_with("Only one flag must be specified (--human or --inode)")


if __name__ == '__main__':
    unittest.main()
