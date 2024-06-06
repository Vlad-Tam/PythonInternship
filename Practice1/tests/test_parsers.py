import unittest
from parser_base import ParserBase
from parser_human import ParserHuman
from parser_inode import ParserInode


class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser_base = ParserBase()
        self.parser_human = ParserHuman()
        self.parser_inode = ParserInode()

    def test_base_parse_output(self):
        output = 'Файл.система   1K-блоков Использовано Доступно Использовано% Cмонтировано в\ntmpfs            ' \
                 '1616208         2340  1613868            1% /run'
        expected_result = [
            {
                "Файл.система": "tmpfs",
                "1K-блоков": "1616208",
                "Использовано": "2340",
                "Доступно": "1613868",
                "Использовано%": "1%",
                "Cмонтировано": "/run"
            }]
        self.assertEqual(self.parser_base.parse_output(output), expected_result)

    def test_human_parse_output(self):
        output = 'Файл.система   Размер Использовано  Дост Использовано% Cмонтировано в\ntmpfs            1,' \
                 '6G         2,3M  1,6G            1% /run'
        expected_result = [
            {
                "Файл.система": "tmpfs",
                "Размер": "1,6G",
                "Использовано": "2,3M",
                "Дост": "1,6G",
                "Использовано%": "1%",
                "Cмонтировано": "/run"
            }]
        self.assertEqual(self.parser_human.parse_output(output), expected_result)

    def test_inode_parse_output(self):
        output = 'Файл.система    Iнодов IИспользовано IСвободно IИспользовано% Cмонтировано в\ntmpfs          ' \
                 '2020257          1449   2018808             1% /run'
        expected_result = [
            {
                "Файл.система": "tmpfs",
                "Iнодов": "2020257",
                "IИспользовано": "1449",
                "IСвободно": "2018808",
                "IИспользовано%": "1%",
                "Cмонтировано": "/run"
            }]
        self.assertEqual(self.parser_inode.parse_output(output), expected_result)


if __name__ == "__main__":
    unittest.main()
