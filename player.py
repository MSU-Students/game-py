from abc import abstractmethod
from utils import clear_console, goto_xy
from element import Element
from animation_frame import AnimationFrame
from amo import Amo
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
        self.amos = []
        self.life = 1

    def __secret(self): 
        return f'{self.age}{self.first_name[0]}'
    
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

    def nextFrame(self, screen):
        for amo in self.amos:
            amo.nextFrame(screen)

    def display(self):
        goto_xy(self._position)
        print(self._avatar, end='')

    def setRemainingLife(self, life: int):
        self.life = life

class EnemyPlayer(BasePlayer):
    life = 100
    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        self._avatar = '[*]'
    def decrementLife(self):
        self.life = self.life - 1
    def getType():
        return 'Enemy'
    def fullName(self, separator=' '):
        return f'[Enemy] {super().fullName(separator)}'
    

#AirPlaneStates
STEADY = -1
GOING_LEFT = 0
GOING_RIGHT = 1
GOING_UP = 2

class AirPlane(BasePlayer, AnimationFrame):
    kill = 0
    state = STEADY
    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        self._avatar = '[8]'
        self.loadAnimation('./animations/plane.txt')
    def incrementKill(self, enemy: EnemyPlayer):
        self.kill = self.kill + 1
        enemy.decrementLife()
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
    def getFrame(self):
        if (self.state == STEADY):
            return super().getFrame()
        else:
            frame = self.getAnimationFrame()
            if (frame == False):
                if (self.state == GOING_RIGHT):
                    self.movePosition((2, 0))
                elif (self.state == GOING_LEFT):
                    self.movePosition((-2, 0))
                elif (self.state == GOING_UP):
                    self.movePosition((0, -1))
                self.state = STEADY
                return super().getFrame()
            else:
                return (self._position[0], self._position[1], frame)
            


