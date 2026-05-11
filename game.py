from pynput import keyboard
from player import AirPlane, EnemyPlayer
from screen import Screen
from utils import sleep
from game_navigation import GameNavigation
from game_story import GameStory
from game_animation import GameAnimation
from game_levels import GameLevels
from game_profile import GameProfile
from waves import Waves
class InvalidFirstNameError(Exception):
    message = 'No First name provided'
    def __init__(self, msg:str = ''):
        super().__init__(msg)
        self.message = msg if msg != '' else self.message

class Game(GameNavigation, GameStory, GameAnimation, GameLevels, GameProfile):
    screen = Screen()
    wave = Waves()
    __index = 0 # step 1
    def __init__(self, firstName:str, lastName):
        super().__init__()
        if firstName == '':
            raise InvalidFirstNameError()
        elif firstName.isdigit():
            raise InvalidFirstNameError('Number Name')
        self.mainPlayer = AirPlane(firstName, lastName)
        self.enemies = self.wave.enemies
        # self.enemies = [
        #     EnemyPlayer('Black', 'Bird'),
        #     EnemyPlayer('Enel', 'God'),
        #     EnemyPlayer('Goku', 'YellowHair')
        # ]
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
    def onPress(self, key:keyboard.KeyCode):
        try:
            if hasattr(key, 'char') and key.char is not None and key.char.lower() == 'p':
                self.paused = not self.paused
            if (self.paused): 
                return 
            if key == keyboard.Key.up:
                self.mainPlayer.goUp()
            elif key == keyboard.Key.down:
                self.mainPlayer.goDown()
            elif key == keyboard.Key.right:
                self.mainPlayer.glideRight()
            elif key == keyboard.Key.left:
                self.mainPlayer.glideLeft()
            elif key == keyboard.Key.space:
                self.mainPlayer.fire()
            elif key == keyboard.Key.esc:
                self.listener.stop()
        except Exception as e:
            self.pauseMessage = f'Something went wrong: {e}'
            self.paused = True

    def play(self):
        self.listener.start()
        
        self.welcomeScreen()
        userName = self.profileInput()

        
        
        #self.mainPlayer.drawElement(self.screen)
        self.loadMainPlayer(userName)
        self.loadEnemies()
        #self.enemies[0].setPosition((30, 10))


        
        #self.enemies[0].drawElement(self.screen)
        #self.screen.printScreen()

        self.loadingScreen() #will loads the game before it strts




        # Start Getting Input
        
        self.startGame()

        self.on_press()
        self.exitGame()


        
        

        