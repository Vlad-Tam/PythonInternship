import subprocess
from typing import Union, List, Dict

from parser_base import ParserBase
from parser_human import ParserHuman
from parser_inode import ParserInode


class ExecutorBase:

    def __init__(self, parser: Union[ParserBase, ParserHuman, ParserInode], command: List = ['df']):
        self.__parser = parser
        self.__command = command

    @property
    def parser(self) -> Union[ParserBase, ParserHuman, ParserInode]:
        return self.__parser

    @parser.setter
    def parser(self, parser: Union[ParserBase, ParserHuman, ParserInode]) -> None:
        self.__parser = parser

    @property
    def command(self) -> List:
        return self.__command

    @command.setter
    def command(self, command: List) -> None:
        self.__command = command

    def execute(self) -> Dict:
        try:
            process = subprocess.Popen(self.__command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            return_code = process.returncode
            if return_code == 0:
                return {
                    'status': 'Success',
                    'error': 'None',
                    'result': self.__parser.parse_output(stdout.decode())
                }
            else:
                return {
                    'status': 'Failure',
                    'error': stderr.decode().strip(),
                    'result': 'None'
                }
        except subprocess.CalledProcessError as e:
            return {
                'status': 'Failure',
                'error': str(e),
                'result': 'None'
            }
