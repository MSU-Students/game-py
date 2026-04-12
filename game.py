from pynput import keyboard
from player import AirPlane, EnemyPlayer
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
        self.mainPlayer = AirPlane(firstName, lastName)
        self.enemies = [
            EnemyPlayer('Black', 'Bird'),
            EnemyPlayer('Enel', 'God')
        ]
        self.listener = keyboard.Listener(on_press=self.onPress)
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
    def onPress(self, key):
        try:
            if key == keyboard.Key.up:
                self.mainPlayer.movePosition((0, -1))
            elif key == keyboard.Key.down:
                self.mainPlayer.movePosition((0, 1))
            elif key == keyboard.Key.right:
                self.mainPlayer.movePosition((1, 0))
            elif key == keyboard.Key.left:
                self.mainPlayer.movePosition((-1, 0))
            elif key == keyboard.Key.esc:
                self.listener.stop()
        except:
            print('Something went wrong')
    def play(self):
        self.listener.start()
        PIXELS = 2
        X_COORDINATE = 0
        Y_COORDINATE = 1
        self.screen.drawStringAt(3, 4, 'Welcome to GAME PY')
        self.mainPlayer.setPosition((10, 10))
        frame = self.mainPlayer.getFrame()
        self.screen.drawPixelsAt(frame[PIXELS], frame[X_COORDINATE], frame[Y_COORDINATE] )
        self.screen.printScreen()
        sleep(1)
        self.enemies[0].setPosition((5, 1))
        eFrame = self.enemies[0].getFrame()
        self.screen.drawPixelsAt(eFrame[PIXELS], eFrame[X_COORDINATE], eFrame[Y_COORDINATE] )
        self.screen.printScreen()

        # Start Getting Input
        
        while self.listener.running:            
            self.screen.clearScreen()
            self.screen.drawFrame()
            frame = self.mainPlayer.getFrame()
            try:
                self.screen.drawPixelsAt(frame[PIXELS], frame[X_COORDINATE], frame[Y_COORDINATE] )
            except:
                print('Something went wrong')
                sleep(1)
            self.screen.printScreen()
            sleep(0.2)
        print('Good Bye')


        
        

        