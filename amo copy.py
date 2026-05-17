from element import Element
class Amo(Element):
    def __init__(self, position:tuple):
        super().__init__([['*']])
        self.setPosition(position)
    
    def nextFrame(self, screen):
        if (self._position[1] > 0):
            self.movePosition((0, -1))