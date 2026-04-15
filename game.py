from pynput import keyboard
from player import AirPlane, EnemyPlayer
from screen import Screen
from utils import sleep
from game_navigation import GameNavigation
from game_story import GameStory
from game_animation import GameAnimation
from game_levels import GameLevels
from game_profile import GameProfile
class InvalidFirstNameError(Exception):
    message = 'No First name provided'
    def __init__(self, msg:str = ''):
        super().__init__(msg)
        self.message = msg if msg != '' else self.message

class Game(GameNavigation, GameStory, GameAnimation, GameLevels, GameProfile):
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
            elif key == keyboard.Key.space:
                self.mainPlayer.fire()
            elif key == keyboard.Key.esc:
                self.listener.stop()
        except:
            print('Something went wrong')
    def play(self):
        self.listener.start()
        
        self.welcomeScreen()
        userName = self.profileInput()
        
        # self.mainPlayer.drawElement(self.screen)
        self.loadMainPlayer(userName)

        self.enemies[0].setPosition((5, 1))
        
        # self.enemies[0].drawElement(self.screen)
        # self.screen.printScreen()

        # Start Getting Input
        
        self.startGame()

        self.exitGame()


        
        

        