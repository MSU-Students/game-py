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
    
    def onPress(self, key:keyboard.KeyCode):
        try:
            if hasattr(key, 'char') and key.char is not None and key.char.lower() == 's':
                self.saveCurrentGame()
                return
                 
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

    def beforeNextFrame(self):
        self.checkCollisions()
    
    def afterNextFrame(self):
        self.eliminateDeads()
        for enemy in self.waves.enemies:
            if (hasattr(enemy, 'moveEnemy')):
                enemy.moveEnemy(self.mainPlayer._position[0])
    
    def play(self):
        self.listener.start()
        
        self.welcomeScreen()
         saved_name = self.mainMenu()
        
        if saved_name is None:
            userName = self.profileInput()
            self.chooseDifficulty()
            self.setupGame()
            self.spawnGameBasedOnDiff()
            self.loadMainPlayer(userName)
        else:
            self.setupGame()
            self.spawnGameBasedOnDiff()
            self.loadMainPlayer(saved_name)
        
        self.loadingScreen() 
        
        self.startGame()

        self.exitGame()

    




        
        

        
