import random
from src.components.animation_frame import AnimationFrame
from src.components.player import BasePlayer, STEADY, GOING_LEFT, GOING_RIGHT
from src.components.element import Element
from src.utils import TimeClass

class EnemyPlayer(BasePlayer, Element):
    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        Element.__init__(self, [
            ['\\','|',' ','|', '/'],
            [' ','\\',' ','/',' '],
            [' ',' ','v',' ',' ']
        ])
        #Amo.nextFrame
        self.life = 100
        self.targetDirectionX: int # Determines the x-direction of the main player from enemy
        self.mainPlayerDir: str = "middle"# "left" or "right" or "middle" direction of the main player from enemy
        self.moveSpeed: int
        self.allowEnemyFire: bool = True # Allows enemy firing, this is to ensure that it doesn't fire endlessly
        self.enemyTimer = TimeClass()
        self._avatar = '[*]'
        self.moveSpeed = 1 # The movement speed of the enemy by default
        self.randomizer = random.Random()
        self.randomCoolDown: float = self.randomizer.uniform(1.5, 5.0) # randomizes the cooldown each movement of the enemy


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
        self.enemyTimer.timeCheck()
        self.enemyTimer.startTimer(self.randomCoolDown)
        self.enemyTimer.timerFinished()
        self.targetDirectionX = mainPlayerPosX - self._position[0] # Determines the x-direction of the player
        
        #Determines the direction of the main Player every once in a while
        if self.enemyTimer.currentTime >= self.enemyTimer.targetTime - 0.5 and self.enemyTimer.currentTime <= self.enemyTimer.targetTime:
            self.randomCoolDown: float = self.randomizer.uniform(1.5, 5.0)
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
   
  

class Enemy03(BasePlayer, AnimationFrame):
    life = 1
    alive = True
    _current_frame = None

    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        self._avatar = '[E3]'
        self.loadAnimation('./animations/enemy03.txt')
        try:
            self.setState(0)
        except Exception:
            pass
        if hasattr(self, 'peekAnimationFrame'):
            self._current_frame = self.peekAnimationFrame()
        else:
            f = self.getAnimationFrame()
            if f:
                self._current_frame = f
                try:
                    self.setState(0)
                except Exception:
                    pass

    def decrementLife(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.alive = False

    def is_alive(self):
        return getattr(self, 'alive', True)

    def getType(self):
        return 'Enemy03'

    def fullName(self, separator=' '):
        return f'[Enemy03] {super().fullName(separator)}'

    def nextFrame(self, screen):
        if not self.is_alive():
            return
        frame = self.getAnimationFrame()
        if frame == False:
            try:
                self.setState(0)
            except Exception:
                pass
            frame = self.getAnimationFrame()
        if frame:
            self._current_frame = frame
        self.movePosition((0, 1))

    def getFrame(self):
        if not self.is_alive():
            return False
        if self._current_frame is None:
            if hasattr(self, 'peekAnimationFrame'):
                self._current_frame = self.peekAnimationFrame()
        return (self._position[0], self._position[1], self._current_frame if self._current_frame is not None else [[]])

    def get_hit_coords(self):
        pixels = self._current_frame
        if pixels is None:
            if hasattr(self, 'peekAnimationFrame'):
                pixels = self.peekAnimationFrame()
        if not pixels:
            return set()
        x, y = self._position
        coords = set()
        for ry, row in enumerate(pixels):
            for rx, ch in enumerate(row):
                if ch != ' ':
                    coords.add((x + rx, y + ry))
        return coords


class DescendingEnemy(BasePlayer):
    """An enemy that starts at the top and descends one row per frame. Dies in one hit."""
    life = 1
    alive = True

    def __init__(self, fName='', lName='', pixels=None):
        # initialize BasePlayer fields
        super().__init__(fName, lName)
        # override sprite pixels
        if pixels is None:
            pixels = [
                [' ', 'V', ' '],
                ['/', '|', '\\']
            ]
        try:
            self._Element__pixels = pixels
        except Exception:
            # fallback: call Element.__init__ if available
            try:
                Element.__init__(self, pixels)
            except Exception:
                pass

    def getType(self):
        return 'DescendingEnemy'

    def is_alive(self):
        return getattr(self, 'alive', True)

    def decrementLife(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.alive = False

    def getFrame(self):
        if not self.is_alive():
            return False
        self.movePosition((0, 1))
        pixels = getattr(self, '_Element__pixels', None)
        if pixels is None:
            return super().getFrame()
        return (self._position[0], self._position[1], pixels)

    def get_hit_coords(self):
        pixels = getattr(self, '_Element__pixels', None)
        if pixels is None:
            f = super().getFrame()
            if not f:
                return set()
            x, y, pixels = f
        x, y = self._position
        coords = set()
        for ry, row in enumerate(pixels):
            for rx, ch in enumerate(row):
                if ch != ' ':
                    coords.add((x + rx, y + ry))
        return coords

