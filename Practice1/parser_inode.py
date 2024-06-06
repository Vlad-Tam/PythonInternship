from parser_base import ParserBase


class ParserInode(ParserBase):
    """
    OUTPUT_FORMAT = ('Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on')
    Works similarly to parser_base, open for extension
    """
