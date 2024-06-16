import subprocess


class SSHPass:

    PASSWORD_PATH = './password.txt'

    def __init__(self, host, username, password=None, subcommand='ssh'):
        self.__host = host
        self.__username = username
        self.__subcommand = subcommand
        self.__password = password

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, value: str):
        self.__host = value

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str):
        self.__username = value

    @property
    def subcommand(self) -> str:
        return self.__subcommand

    @subcommand.setter
    def subcommand(self, value: str):
        self.__subcommand = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str):
        self.__password = value

    def run_command(self, command):
        try:
            if self.__password is not None:
                process = subprocess.Popen(
                    f'sshpass -p {self.__password} {self.__subcommand} {self.__username}@{self.__host}'
                    f'{self.check_subcommand()}{command}',
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                )
                # print(f"COMMAND: 'sshpass -p {self.__password} {self.__subcommand} {self.__username}@{self.__host}
                # {self.check_subcommand()}{command}'")
            else:
                process = subprocess.Popen(
                    f'sshpass -f {self.PASSWORD_PATH} {self.__subcommand} {self.__username}@{self.__host}'
                    f'{self.check_subcommand()}{command}',
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                )
            stdout, stderr = process.communicate()
            return_code = process.returncode
            return {'stdout': stdout.decode().strip(), 'stderr': stderr.decode().strip(), 'return code': return_code}
        except subprocess.CalledProcessError as e:
            return {'stdout': e.output.decode().strip(), 'stderr': e.stderr.decode().strip(),
                    'return code': e.returncode}

    def check_subcommand(self):
        if self.__subcommand == 'scp':
            return ':'
        else:
            return ' '
