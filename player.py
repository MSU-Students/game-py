from abc import ABC, abstractmethod
from utils import clear_console, goto_xy
 
class BasePlayer(ABC):
    __pixels = [
        [' ',' ','^',' ', ' '],
        [' ','/',' ','\\',' '],
        ['/','|',' ','|','\\']
    ]

    def getFrame(self):
        return (self.__position[0], self.__position[1], self.__pixels)
    # Constructor
    def __init__(self, fName = '', lName = ''):
        self.first_name = fName
        self.last_name = lName
        self.__position = (0, 0)
        self._avatar = '[A]'

    def __secret(self): 
        return f'{self.age}{self.first_name[0]}'
    
    @abstractmethod
    def getType():
        pass

    @abstractmethod
    def fullName(self, separator = ' '):
        return f'{self.first_name}{separator}{self.last_name}'

    def setPosition(self, position):
        self.__position = (position[0], position[1])
    def movePosition(self, coordinates:tuple): 
        newX = self.__position[0] + coordinates[0]
        newY = self.__position[1] + coordinates[1]
        self.__position = (newX, newY)
    def display(self):
        goto_xy(self.__position)
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


