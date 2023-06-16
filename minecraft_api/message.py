class message:
    def __init__(self):
        '''
        Creating a new message
        '''
        self.message = []
    def runCommand(self, text, command, hover=None):
        '''
        Run command as user after click
        :param str text: Message text
        :param str command: Command what execute after click
        :param str hover: Output on hover (optional)
        '''
        data = {'text': text, 'clickevent': {'action': 'run_command', 'value': f'/{command}'}}
        if hover != None:
            data['hoverEvent'] = {'action': 'show_text', 'contents': hover}
        self.message.append(data)
    def suggestCommand(self, text, command, hover=None):
        '''
        Suggest command to user after click
        :param str text: Message text
        :param str command: Command what suggest after click
        :param str hover: Output on hover (optional)
        '''
        data = {'text': text, 'clickevent': {'action': 'suggest_command', 'value': f'/{command}'}}
        if hover != None:
            data['hoverEvent'] = {'action': 'show_text', 'contents': hover}
        self.message.append(data)
    def suggestMessage(self, text, message, hover=None):
        '''
        Suggest message to user after click
        :param str text: Message text
        :param str message: Message what suggest after click
        :param str hover: Output on hover (optional)
        '''
        data = {'text': text, 'insertion': message}
        if hover != None:
            data['hoverEvent'] = {'action': 'show_text', 'contents': hover}
        self.message.append(data)
    def copyToClipboard(self, text, clipboard, hover=None):
        '''
        Copy something to user clipboard after click
        :param str text: Message text
        :param str clipboard: Something what copying after click
        :param str hover: Output on hover (optional)
        '''
        data = {'text': text, 'clickevent': {'action': 'copy_to_clipboard', 'value': clipboard}}
        if hover != None:
            data['hoverEvent'] = {'action': 'show_text', 'contents': hover}
        self.message.append(data)
    def openUrl(self, text, url, hover=None):
        '''
        Suggest to open url after click
        :param str text: Message text
        :param str url: Url what opens after click
        :param str hover: Output on hover (optional)
        '''
        data = {'text': text, 'clickevent': {'action': 'open_url', 'value': url}}
        if hover != None:
            data['hoverEvent'] = {'action': 'show_text', 'contents': hover}
        self.message.append(data)
    def default(self, text, hover=None):
        '''
        Standart text
        :param str text: Message text
        :param str hover: Output on hover (optional)
        '''
        data = {'text': text}
        if hover != None:
            data['hoverEvent'] = {'action': 'show_text', 'contents': hover}
        self.message.append(data)
    def sendMessage(self, mc):
        '''
        Send this message
        :param func mc: Minecraft session
        '''
        message = str(self.message).replace("'", '"')
        mc.sendCommand(f'tellraw @a {message}')