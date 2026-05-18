from abc import abstractmethod, ABC
from pynput import keyboard
from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.enemy_player import EnemyPlayer
from src.components.player import AirPlane, BasePlayer
import src.modules.game_levels as game_levels
from src.modules.game_levels import GameLevels
from src.components.waves import Waves
from ..utils import TimeClass

class GameNavigation(ABC):
    timeClass = TimeClass()
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener
    waves: Waves
    paused: bool
    pauseMessage: str
    gameLevels: GameLevels
    def __init__(self):
        self.allowDisplayNextWave: bool = False
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
    
    def chooseDifficulty(self):
        difficultyInput: str = '0' # Default value, will be changed.
        difficultyString: str = ' ' # This will display the difficulty
        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Choose Difficulty (1-EASY, 2-MODERATE, 3-HARD): ')
        self.screen.printScreen()
        goto_xy((3, 12))
        difficultyInput = input()
        while difficultyInput not in ['1', '2', '3']:
            self.resetScreen()
            self.screen.drawStringAt(3, 10, 'Invalid input...')
            self.screen.printScreen()
            sleep(1)
            self.resetScreen()
            self.screen.drawStringAt(3, 10, 'Choose Difficulty (1-EASY, 2-MODERATE, 3-HARD): ')
            self.screen.printScreen()
            goto_xy((3, 12))
            difficultyInput = input()
            
        # /////////////////////////////////////////////////////////////////////////////
        if difficultyInput == '1':
            game_levels.currentDifficulty = game_levels.EASY
            difficultyString = 'EASY'
        elif difficultyInput == '2':
            game_levels.currentDifficulty = game_levels.MODERATE
            difficultyString = 'MODERATE'
        elif difficultyInput == '3':
            game_levels.currentDifficulty = game_levels.HARD
            difficultyString = 'HARD'
        # /////////////////////////////////////////////////////////////////////////////

        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Chosen difficulty: ' + difficultyString)
        self.screen.printScreen()
        sleep(3)
    
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
    
    def displayNextWave(self): # After all enemies are unalived, display the next wave.
        self.timeClass.timeCheck()
        if len(self.enemies) == 0 and self.allowDisplayNextWave == False:
            self.allowDisplayNextWave = True
        if self.allowDisplayNextWave == True:
            self.timeClass.startTimer(3.0)
            self.timeClass.timerFinished()
            if self.timeClass.timerFinished() != True:
                self.screen.drawStringAt(32, 15, f"Wave Number: {self.waves.currentWave}")
            else:
                self.allowDisplayNextWave = False

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

            if (self.waves.waveChanged == True): # After a wave is complete, configure another wave of enemies.
                if (self.timeClass.timerFinished() == True): # References of self.timeClass methods are in the displayNextWave().
                    self.gameLevels.spawnGameBasedOnDiff(self)       

            self.displayLife()
            self.displayDifficulty(1)
            self.displayNextWave()
            self.screen.printScreen()
            self.waves.nextWave()
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
