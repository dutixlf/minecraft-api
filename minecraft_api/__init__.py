from mcrcon import MCRcon
from pathlib import Path
from getpass import getpass
import minecraft_api.server as server
import minecraft_api.world as world

class Connect:
    def __init__(self, session='session', World='overworld'):
        '''
        Creating/Connecting to session.
        :param str session: Session's name
        :param str world: Default world to command execution
        '''
        self.session = session
        if Path(f'{session}.session').is_file():
            with open(f'{session}.session', 'r+') as f:
                data = str(f.read()).split('\n')
                host=data[0]
                password=data[1]
                port=int(data[2])
                self.Connection = MCRcon(host=host, password=password, port=port)
                self.Connection.connect()
        else:
            with open(f'{session}.session', 'w+') as f:
                host = str(input('Enter hostname: '))
                port = int(input('Enter port: '))
                password = getpass('Enter password: ')
                f.write(f'{host}\n{password}\n{port}')
            self.Connection = MCRcon(host=host, password=password, port=port)
            self.Connection.connect()
            self.Connection.command('gamerule sendCommandFeedback false')

        self.Server = server.Server(self.Connection)
        self.World = world.World(self.Connection, f'minecraft:{World.replace("minecraft:", "")}')
    def sendCommand(self, cmd=str):
        '''
        Send command as RCON
        :param str cmd: Command what you want to send
        '''
        req = self.Connection.command(cmd)
        return req