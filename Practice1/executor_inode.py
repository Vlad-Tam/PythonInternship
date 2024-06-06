from typing import Union

from executor_base import ExecutorBase

from parser_base import ParserBase
from parser_human import ParserHuman
from parser_inode import ParserInode


class ExecutorInode(ExecutorBase):

    def __init__(self, parser: Union[ParserBase, ParserHuman, ParserInode]):
        super().__init__(parser)
        self.command.append('-i')
