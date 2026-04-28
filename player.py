from abc import abstractmethod
from utils import clear_console, goto_xy, TimeClass
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
            amo.nextFrame(screen, 0, -1)

    def display(self):
        goto_xy(self._position)
        print(self._avatar, end='')

    def setRemainingLife(self, life: int):
        self.life = life

class EnemyPlayer(BasePlayer, Element):
    enemyTimer = TimeClass
    life = 100
    targetDirectionX: int # Determines the x-direction of the main player from enemy
    mainPlayerDir: str = "middle"# "left" or "right" or "middle" direction of the main player from enemy
    moveSpeed: int
    allowEnemyFire: bool = True # Allows enemy firing, this is to ensure that it doesn't fire endlessly
    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        Element.__init__(self, [
            ['\\','|',' ','|', '/'],
            [' ','\\',' ','/',' '],
            [' ',' ','v',' ',' ']
        ])
        #Amo.nextFrame
        self._avatar = '[*]'
        self.moveSpeed = 1 # The movement speed of the enemy by default

    def decrementLife(self):
        self.life = self.life - 1
    def getType():
        return 'Enemy'
    def fullName(self, separator=' '):
        return f'[Enemy] {super().fullName(separator)}'
    def fire(self):
        self.amos.append(Amo((self._position[0] + 2, self._position[1] + 1)))
    def nextFrame(self, screen):
        for amo in self.amos:
            amo.nextFrame(screen, 0, 1)
    def moveEnemy(self, mainPlayerPosX: int): # Moves enemy when called
        self.enemyTimer.timeCheck(self.enemyTimer)
        self.enemyTimer.startTimer(self.enemyTimer, 5)
        self.enemyTimer.timerFinished(self.enemyTimer)
        self.targetDirectionX = mainPlayerPosX - self._position[0] # Determines the x-direction of the player
        
        #Determines the direction of the main Player every once in a while
        if self.enemyTimer.currentTime >= self.enemyTimer.targetTime - 0.5 and self.enemyTimer.currentTime <= self.enemyTimer.targetTime:
            if self.targetDirectionX < 0: 
                self.mainPlayerDir = "left"
            elif self.targetDirectionX > 0: 
                self.mainPlayerDir = "right"
            else: 
                self.mainPlayerDir = "middle"

            if self.allowEnemyFire == True:
                self.fire()
                self.allowEnemyFire = False
        elif self.enemyTimer.currentTime < self.enemyTimer.targetTime and self.allowEnemyFire == False:
            self.allowEnemyFire = True


        #Moves the enemy according to the direction of the main Player
        if self.enemyTimer.currentTime <= self.enemyTimer.targetTime - 2:
            if self.mainPlayerDir == "left": # If main Player is on the left of the enemy, move left
                self.movePosition((-self.moveSpeed, 0))
            elif self.mainPlayerDir == "right": # if main Player is on the right of the enemy, move right
                self.movePosition((self.moveSpeed, 0))
            elif self.mainPlayerDir == "middle": # if main Player is neither left nor right, remain steady
                self.movePosition((0, 0))
   
    

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
    def goDown(self):
        self.state = GOING_DOWN
        self.setState(GOING_DOWN)
    def getFrame(self):
        if (self.state == STEADY):
            return super().getFrame()
        else:
            frame = self.getAnimationFrame()
            if (frame == False):
                self.state = STEADY
                return super().getFrame()
            else:
                if (self.state == GOING_RIGHT):
                    self.movePosition((1, 0))
                elif (self.state == GOING_LEFT):
                    self.movePosition((-1, 0))
                elif (self.state == GOING_UP):
                    self.movePosition((0, -1))
                elif (self.state == GOING_DOWN):
                    self.movePosition((0, 1))
                return (self._position[0], self._position[1], frame)
            