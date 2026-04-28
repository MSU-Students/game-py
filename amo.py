from element import Element
class Amo(Element):
    def __init__(self, position:tuple):
        super().__init__([['*']])
        self.setPosition(position)
    
    def nextFrame(self, screen, moveposX:int = 0, moveposY:int = -1):
        if (self._position[1] > 0):
            self.movePosition((moveposX, moveposY))