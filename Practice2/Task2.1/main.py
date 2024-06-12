from sshpass import SSHPass

if __name__ == "__main__":
    ssh_client = SSHPass(host='192.168.1.102', username='root')

    while True:
        result = ssh_client.run_command(input(f'SSH:>'))
        print(f'{result}')
