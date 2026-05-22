from pynput import keyboard

from src.utils import sleep
from src.components.player import AirPlane
from src.components.enemy_player import Enemy03
from src.core.screen import Screen
from src.components.waves import Waves
from src.modules.game_navigation import GameNavigation
from src.modules.game_story import GameStory
from src.modules.game_animation import GameAnimation
from src.modules.game_levels import GameLevels
from src.modules.game_profile import GameProfile

class InvalidFirstNameError(Exception):
    message = 'No First name provided'
    def __init__(self, msg:str = ''):
        super().__init__(msg)
        self.message = msg if msg != '' else self.message

class Game(GameNavigation, GameStory, GameAnimation, GameLevels, GameProfile):
    screen = Screen()
    __index = 0 # step 1
    def __init__(self):
        super().__init__()
        self.waves = Waves(self.screen)
        self.gameLevels = GameLevels
        self.mainPlayer = AirPlane()
        self.waves.spawn_enemy()
        self.enemies = self.waves.enemies
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
                 self.mainPlayer.goUp()

             elif key == keyboard.Key.down:
                 self.mainPlayer.goDown()

             elif key == keyboard.Key.right:
              self.mainPlayer.glideRight()

             elif key == keyboard.Key.left:
                 self.mainPlayer.glideLeft()

        # TRY AGAIN
             elif hasattr(key, 'char') and key.char == 'r':
                 self.mainPlayer._position = (10, 10)

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
        self.chooseDifficulty()
        
        self.loadMainPlayer(userName)
        self.mainPlayer._position = (10, 10)
        self.enemies[0].setPosition((5, 1))
        
        self.startGame()

        self.exitGame()

    




        
        

        