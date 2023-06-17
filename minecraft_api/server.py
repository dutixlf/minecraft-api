class Server:
    def __init__(self, mc):
        '''
        Setup connection with rcon
        :param func mc: Rcon connection variable
        '''
        self.mc = mc
    def players(self):
        '''
        Get players on server
        '''
        data = str(self.mc.command('list')).split(': ')
        players = str(data[1]).split(', ')
        return players
    def kick(self, players, reason='Kicked by Minecraft_api'):
        for player in players:
            self.mc.command(f'kick {player} {reason}')
    def ban(self, players, reason='Kicked by Minecraft_api'):
        for player in players:
            self.mc.command(f'ban {player} {reason}')
    def unban(self, players):
        for player in players:
            self.mc.command(f'pardon {player}')
    def plugins(self):
        pl = str(self.mc.command(f'plugins')).split(': ')
        pl = pl[1].split('§f, ')
        enabled = []
        disabled = []
        for plugin in pl:
            if '§a' in plugin:
                enabled.append(plugin.replace('§a', ''))
            if '§c' in plugin:
                disabled.append(plugin.replace('§c', ''))
        plugins = {
            'enabled': enabled,
            'disabled': disabled
        }
        return plugins