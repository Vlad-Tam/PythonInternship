import subprocess


class SSHPass:

    PASSWORD_PATH = './password.txt'

    def __init__(self, host, username, password=None, subcommand='ssh'):
        self.__host = host
        self.__username = username
        self.__subcommand = subcommand
        self.__password = password

    def run_command(self, command):
        try:
            process = None
            if self.__password is not None:
                process = subprocess.Popen(
                    f'sshpass -p {self.__password} {self.__subcommand} {self.__username}@{self.__host}{self.check_subcommand()}{command}',
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                )
            else:
                process = subprocess.Popen(
                    f'sshpass -f {self.PASSWORD_PATH} {self.__subcommand} {self.__username}@{self.__host}{self.check_subcommand()}{command}',
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                )
            stdout, stderr = process.communicate()
            return_code = process.returncode
            return {'stdout': stdout.decode().strip(), 'stderr': stderr.decode().strip(), 'return code': return_code}
        except subprocess.CalledProcessError as e:
            return {'stdout': e.output.decode().strip(), 'stderr': e.stderr.decode().strip(), 'return code': e.returncode}

    def check_subcommand(self):
        if self.__subcommand == 'scp':
            return ':'
        else:
            return ' '
