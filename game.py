from player import MainPlayer, EnemyPlayer
from screen import Screen
from utils import sleep
class InvalidFirstNameError(Exception):
    message = 'No First name provided'
    def __init__(self, msg:str = ''):
        super().__init__(msg)
        self.message = msg if msg != '' else self.message

class Game:
    screen = Screen()
    __index = 0 # step 1
    def __init__(self, firstName:str, lastName):
        if firstName == '':
            raise InvalidFirstNameError()
        elif firstName.isdigit():
            raise InvalidFirstNameError('Number Name')
        self.mainPlayer = MainPlayer(firstName, lastName)
        self.enemies = [
            EnemyPlayer('Black', 'Bird'),
            EnemyPlayer('Enel', 'God')
        ]
    # called every start of iteration
    def __iter__(self): #step 2
        self.__index = 0
        return self
    
    def __next__(self):#step 3
        if self.__index == 0:
            self.__index += 1
            return self.mainPlayer
        elif self.__index <= self.enemies.__len__():
            self.__index += 1
            return self.enemies[self.__index - 2]
        else:
            raise StopIteration #step 4
        
    def play(self):
        
        self.screen.drawCharAt(5, 5)
        self.screen.printScreen()
        sleep(1)
        self.screen.drawCharAt(5, 6)
        self.screen.printScreen()
        sleep(1)
        self.screen.drawCharAt(6, 7)
        self.screen.printScreen()
        sleep(1)