class Parser:

    @staticmethod
    def get_bandwidth_from_iperf(data):
        rows = data.strip().split('\n')
        values = rows[6].split()
        for i in range(len(values)):
            if values[i].__eq__("Gbits/sec") or values[i].__eq__("Mbits/sec"):
                return f'{values[i-1]} {values[i]}'
        return None
