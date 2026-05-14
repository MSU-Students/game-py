from abc import abstractmethod, ABC
from pynput import keyboard
from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.enemy_player import EnemyPlayer
from src.components.player import AirPlane, BasePlayer
import src.modules.game_levels as game_levels
from src.components.waves import Waves

class GameNavigation(ABC):
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener
    waves: Waves
    paused: bool
    pauseMessage: str
    def __init__(self):
        self.paused = False
        self.pauseMessage = ''
    def welcomeScreen(self):
        self.screen.drawStringAt(31, 17, 'Welcome to GAME PY')
        self.screen.printScreen()
        sleep(3)

    def resetScreen(self):
        self.screen.clearScreen()
        self.screen.drawFrame()

    def displayLife(self): #This will display the Health of the player while playing
        self.screen.drawStringAt(65 , 32, f'life: {str(self.mainPlayer.life)}')

    def profileInput(self):
        self.resetScreen()
        self.screen.drawStringAt(32, 17, 'Enter Your Name:')
        self.screen.printScreen()
        goto_xy((33, 19))
        user = input()
        self.resetScreen()
        self.screen.drawStringAt(33, 17, 'Welcome ' + user)
        self.screen.printScreen()
        sleep(3)
        return user
    
    def loadingScreen(self):
        self.resetScreen()
        self.blinkText("READY?", 37, 17, 3)
        self.screen.drawStringAt(34, 17, 'Get ready...')
        self.screen.printScreen()
        sleep(1)
 
    def blinkText(self, text = "READY?", x=37, y=17, times=3):
        for i in range(times):
            #show the text
            self.screen.clearScreen()
            self.screen.drawFrame();
            self.screen.drawStringAt(x, y, text)
            self.screen.printScreen()
            sleep(0.5)
            #hide the text
            self.screen.clearScreen()
            self.screen.drawFrame();
            self.screen.printScreen()
            sleep(0.5)

    @abstractmethod
    def beforeNextFrame(self):
        pass
    
    @abstractmethod
    def afterNextFrame(self):
        pass
    
    def startGame(self):
        while self.listener.running:     
            self.screen.clearScreen()
            self.screen.drawFrame()
            if self.paused:
                self.screen.drawStringAt(32, 17, 'PAUSED - Press P')
                if (self.pauseMessage != ''):
                    self.screen.drawStringAt(32, 19, f'Something went wrong: {self.pauseMessage}')
            else:
                self.beforeNextFrame()
                player : BasePlayer   
                for player in self:
                    player.drawElement(self.screen)
                    player.nextFrame(self.screen)
                    
                self.afterNextFrame()
            
            self.displayLife()
            self.displayDifficulty(1)
            self.screen.printScreen()
            sleep(0.1)
                


    def exitGame(self):
        self.screen.drawFrame()
        self.screen.drawStringAt(29, 17, 'Good Bye, from GAME PY')
        self.screen.printScreen()
    

    def displayDifficulty(self, level: int):
        if (level == game_levels.EASY):
            self.screen.drawStringAt(3, 32, 'Difficulty: EASY')
        elif (level == game_levels.MODERATE):
            self.screen.drawStringAt(3, 32, 'Difficulty: MODERATE')
        elif (level == game_levels.HARD):
            self.screen.drawStringAt(3, 32, 'Difficulty: HARD')
