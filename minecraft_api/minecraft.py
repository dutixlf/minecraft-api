from mcrcon import MCRcon
from pathlib import Path
# 6789
class Connect:
    def __init__(self, session='session'):
        self.session = session
        if Path(f'{session}.session').is_file():
            with open(f'{session}.session', 'r+') as f:
                data = str(f.read()).split('\n')
                self.mcr = MCRcon(data[0], data[1], data[2])
                print(self.mcr)
        else:
            with open(f'{session}.session', 'w+') as f:
                host = str(input('Enter hostname: '))
                port = int(input('Enter port: '))
                password = str(input('Enter password: '))
                f.write(f'{host}\n{port}\n{password}')
                self.mcr = MCRcon(host, port, password)
    def sendCommand(self, cmd=str):
        h = self.mcr.command(cmd)
        return h