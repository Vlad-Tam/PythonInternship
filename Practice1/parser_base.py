from typing import List, Dict


class ParserBase:
    """
    OUTPUT_FORMAT = ('Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on')
    """

    def parse_output(self, output: str) -> List[Dict]:
        lines = output.strip().split('\n')
        headers = lines[0].split()
        result = []
        for line in lines[1:]:
            values = line.split()
            row = {headers[i]: value for i, value in enumerate(values)}
            result.append(row)
        return result
