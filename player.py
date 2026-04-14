from abc import abstractmethod
from utils import clear_console, goto_xy
from element import Element
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
    

class AirPlane(BasePlayer):
    kill = 0
    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        self._avatar = '[8]'
    def incrementKill(self, enemy: EnemyPlayer):
        self.kill = self.kill + 1
        enemy.decrementLife()
    def getType():
        return 'Main'
    def fullName(self, separator=' '):
        return f'[Main] {super().fullName(separator)}'


