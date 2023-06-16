from mcrcon import MCRcon
from pathlib import Path

class Connect:
    def __init__(self, session='session', world='overworld'):
        '''
        Creating/Connecting to session.
        session = file with connection data
        :param session: str
        :param world: str
        '''
        self.world = f'minecraft:{world.replace("minecraft:", "")}'
        self.session = session
        if Path(f'{session}.session').is_file():
            with open(f'{session}.session', 'r+') as f:
                data = str(f.read()).split('\n')
                host=data[0]
                password=data[1]
                port=int(data[2])
                self.mcr = MCRcon(host=host, password=password, port=port)
        else:
            with open(f'{session}.session', 'w+') as f:
                host = str(input('Enter hostname: '))
                port = int(input('Enter port: '))
                password = str(input('Enter password: '))
                f.write(f'{host}\n{password}\n{port}')
                self.mcr = MCRcon(host=host, password=password, port=port)
        self.mcr.connect()
        return f'Connected to {host}:{port}'
    def setWorld(self, world='overworld'):
        '''
        Replace command execution world
        :param world: str
        '''
        self.world = f'minecraft:{world.replace("minecraft:", "")}'
        return self.world
    def sendCommand(self, cmd=str):
        '''
        Send command as RCON
        :param cmd: str
        '''
        req = self.mcr.command(f'execute in {self.world} run {cmd}')
        return req