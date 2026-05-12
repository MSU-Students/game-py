from typing import Self
from abc import abstractmethod
from src.core.screen import Screen
from src.utils import goto_xy, TimeClass
from src.components.element import Element
from src.components.animation_frame import AnimationFrame
from src.components.amo import Amo
class BasePlayer(Element):
    # Constructor
    def __init__(self, fName = '', lName = ''):
        super().__init__([
            [' ',' ','^',' ', ' '],
            [' ','/',' ','\\',' '],
            ['/','|',' ','|','\\']
        ])
        self.first_name = fName
        self.last_name = lName
        self._avatar = '[A]'
        self.amos = list[Amo]()
        self.life = 1
        self.alive = True

    def __secret(self): 
        return f'{self.age}{self.first_name[0]}'
    
    def is_alive(self):
        return self.alive
    
    @abstractmethod
    def getType():
        pass

    @abstractmethod
    def fullName(self, separator = ' '):
        return f'{self.first_name}{separator}{self.last_name}'
   
    def fire(self):
        self.amos.append(Amo((self._position[0] + 2, self._position[1] - 1)))
    
    def drawElement(self, screen):
        super().drawElement(screen)
        for amo in self.amos:
            amo.drawElement(screen)

    
    def nextFrame(self, screen: Screen):
        for amo in self.amos:
            amo.nextFrame(screen, 0, -1)

    def display(self):
        goto_xy(self._position)
        print(self._avatar, end='')

    def incrementKill(self, enemy: Self):
        self.kill = self.kill + 1
        enemy.decrementLife()
        
    def decrementLife(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.alive = False
        
    def setRemainingLife(self, life: int):
        self.life = life

    def checkIfColliding(self, counterPlayers: list[Self]):
        for player in counterPlayers:
            collide =  self.isColliding(player.getCoveredCoords())
            if (collide):
                self.decrementLife()
                player.decrementLife()
                return True
            for amo in player.amos:
                collide = self.isColliding(amo.getCoveredCoords())
                if (collide):
                    player.incrementKill(self)
        return False

    



#AirPlaneStates
STEADY = -1
GOING_LEFT = 0
GOING_RIGHT = 1
GOING_UP = 2
GOING_DOWN = 3

class AirPlane(BasePlayer, AnimationFrame):
    kill = 0
    state = STEADY
    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        self._avatar = '[8]'
        self.loadAnimation('./animations/plane.txt')
    
    def getType():
        return 'Main'
    def fullName(self, separator=' '):
        return f'[Main] {super().fullName(separator)}'
    def glideRight(self):
        self.state = GOING_RIGHT
        self.setState(GOING_RIGHT)
    def glideLeft(self):
        self.state = GOING_LEFT
        self.setState(GOING_LEFT)
    def goUp(self):
        self.state = GOING_UP
        self.setState(GOING_UP)
    def goDown(self):
        self.state = GOING_DOWN
        self.setState(GOING_DOWN)
        
    def getFrame(self):
        if (self.state == STEADY):
            return super().getFrame()
        else:
            frame = self.peekAnimationFrame()
            if (frame == False):
                self.state = STEADY
                return super().getFrame()
            else:
                return (self._position[0], self._position[1], frame)
            
    def nextFrame(self, screen: Screen):
        self.getAnimationFrame()
        super().nextFrame(screen)
        if (self.state == GOING_RIGHT):
            screen.drawStringAt(20, 0, 'GOING RIGHT')
            self.movePosition((1, 0))
        elif (self.state == GOING_LEFT):
            screen.drawStringAt(20, 0, 'GOING LEFT')
            self.movePosition((-1, 0))
        elif (self.state == GOING_UP):
            screen.drawStringAt(20, 0, 'GOING UP')
            self.movePosition((0, -1))
        elif (self.state == GOING_DOWN):
            screen.drawStringAt(20, 0, 'GOING DOWN')
            self.movePosition((0, 1))
        
            