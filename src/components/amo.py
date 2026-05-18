from src.components.element import Element
from src.core.screen import Screen

class Amo(Element):
    def __init__(self, position:tuple):
        super().__init__([['*']])
        self.setPosition(position)
        self.alive = True
    
    def nextFrame(self, screen:Screen, moveposX:int = 0, moveposY:int = -1):
        if not self.alive:
            return
        isPlayerAmo = moveposY < 0 
        dim = screen.getDimension()
        if (isPlayerAmo and self._position[1] > 0):
            self.movePosition((moveposX, moveposY))
        elif (not isPlayerAmo and self._position[1] < dim[1]):
            self.movePosition((moveposX, moveposY))
        else:
            self.alive = False
  
