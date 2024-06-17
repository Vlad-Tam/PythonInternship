import threading
import time
from typing import Dict

from sshpass import SSHPass
from parser import Parser


class IperfCommand:

    def __init__(self, ip1, name1, password1, ip2, name2, password2):
        self.__node1 = SSHPass(host=ip1, username=name1, password=password1)
        self.__node2 = SSHPass(host=ip2, username=name2, password=password2)
        self.__parser = Parser()

    @property
    def node1(self) -> SSHPass:
        return self.__node1

    @node1.setter
    def host(self, value: SSHPass):
        self.__node1 = value

    @property
    def node2(self) -> SSHPass:
        return self.__node2

    @node2.setter
    def host(self, value: SSHPass):
        self.__node2 = value

    @property
    def parser(self) -> Parser:
        return self.__parser

    @parser.setter
    def subcommand(self, value: Parser):
        self.__parser = value

    def execute(self):
        print('Starting server')
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()
        server_pid = self.wait_for_server()
        if server_pid == -1:
            return

        print('Starting client')
        client_output = self.run_client()
        self.kill_server_process(server_pid)
        if client_output.get('return code'):
            print(f"ERROR: {client_output.get('stderr')}")
        else:
            client_output['stdout'] = self.__parser.get_fields_from_iperf(client_output.get('stdout'),
                                                                          self.__node1, self.__node2)
            return client_output

    def run_server(self) -> Dict:
        return self.__node1.run_command("iperf -s -1")

    def run_client(self) -> Dict:
        return self.__node2.run_command(f"iperf -c {self.__node1.host} ")

    def wait_for_server(self, timeout: int = 10) -> int:
        for i in range(timeout):
            ps_answer = self.__node1.run_command('ps -C iperf')
            if ps_answer.get('return code') == 0:
                result = ps_answer.get('stdout')
                res_lines = result.splitlines()
                if len(res_lines) == 2:
                    return res_lines[1].split()[0]
            time.sleep(1)
        return -1

    def kill_server_process(self, pid: int) -> Dict:
        return self.__node1.run_command(f'kill {pid}')
