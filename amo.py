from element import Element
class Amo(Element):
    def __init__(self, position:tuple):
        super().__init__([['*']])
        self.setPosition(position)
        self.alive = True
    
    def nextFrame(self, screen):
        if not self.alive:
            return
        if (self._position[1] > 0):
            self.movePosition((0, -1))
        else:
            self.alive = False