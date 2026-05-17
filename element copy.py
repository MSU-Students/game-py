from abc import ABC, abstractmethod

class Element(ABC):
    __pixels = [
        [' '],
    ]

    def __init__(self, pixels):
        self.__pixels = pixels
        self._position = (0, 0)
    
    def getFrame(self):
        return (self._position[0], self._position[1], self.__pixels)

    def setPosition(self, position):
        self._position = (position[0], position[1])
    def movePosition(self, coordinates:tuple): 
        newX = self._position[0] + coordinates[0]
        newY = self._position[1] + coordinates[1]
        self._position = (newX, newY)
    
    def drawElement(self, screen):
        PIXELS = 2
        X_COORDINATE = 0
        Y_COORDINATE = 1
        frame = self.getFrame()
        screen.drawPixelsAt(frame[PIXELS], frame[X_COORDINATE], frame[Y_COORDINATE] )
    
    @abstractmethod
    def nextFrame(self, screen):
        pass