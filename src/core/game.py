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
        
        self.mainPlayer = AirPlane()
        self.enemies = self.waves.enemies
        # spawn initial enemy
        try:
            self.spawn_enemy()
        except Exception:
            # fallback: create directly if spawn_enemy not available
            try:
                e = Enemy03('Waving', 'Enemy')
                self.enemies.append(e)
            except Exception:
                pass
        
        # self.enemies = [
        #     EnemyPlayer('Black', 'Bird'),
        #     EnemyPlayer('Enel', 'God'),
        #     EnemyPlayer('Goku', 'YellowHair')
        # ]
        self.listener = keyboard.Listener(on_press=self.onPress)

    def spawn_enemy(self):
        """Create and position a new Enemy03 at the top-center of the screen."""
        e = Enemy03('Waving', 'Enemy')
        width, height = self.screen.getDimension()
        # try to center enemy (assume width of frame ~3); place at row 1
        e.setPosition((max(1, int(width / 2) - 1), 1))
        try:
            e.setState(0)
        except Exception:
            pass
        self.enemies.append(e)
   
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
        
        
        self.loadMainPlayer(userName)
        self.loadEnemies()
        
        width, _height = self.screen.getDimension()
        # place the descending enemy at top center
        if len(self.enemies) > 0:
            self.enemies[0].setPosition((int(width / 2), 1))
        
        self.loadingScreen() 
        # Start Getting Input and Updating the Screen
        self.startGame()

        self.exitGame()

    




        
        

        