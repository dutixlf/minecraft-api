class World:
    def __init__(self, Connection, World):
        self.Connection = Connection
        self.World = World
    def setWorld(self, world='overworld'):
        self.World = f'minecraft:{world.replace("minecraft:", "")}'
    def setBlock(self, x, y, z, block, data=''):
        '''
        Set block in world
        :arg int x: X coordinate
        :arg int y: Y coordinate
        :arg int z: Z coordinate
        :arg str block: blockid
        :arg str data: Some data :)
        '''
        block = self.Connection.command(f'execute in {self.World} run setblock {x} {y} {z} {block} {data}')
        return block
    def fill(self, x1, y1, z1, x2, y2, z2, block, data=''):
        '''
        Set block in world
        :arg int x1: X1 coordinate
        :arg int y1: Y1 coordinate
        :arg int z1: Z1 coordinate
        :arg int x2: X2 coordinate
        :arg int y2: Y2 coordinate
        :arg int z2: Z2 coordinate
        :arg str block: blockid
        :arg str data: Some data :)
        '''
        block = self.Connection.command(f'execute in {self.World} run fill {x1} {y1} {z1} {x2} {y2} {z2} {block} {data}')
        return block