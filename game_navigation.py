from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane
from pynput import keyboard
import game_levels
class GameNavigation:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener
    def welcomeScreen(self):
        self.screen.drawStringAt(3, 10, 'Welcome to GAME PY')
        self.screen.printScreen()
        sleep(3)

    def resetScreen(self):
        self.screen.clearScreen()
        self.screen.drawFrame()

    def displayLife(self): #This will display the Health of the player while playing
        self.screen.drawStringAt(65 , 2, f'life: {str(self.mainPlayer.life)}')

    def profileInput(self):
        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Enter Your Name:')
        self.screen.printScreen()
        goto_xy((3, 12))
        user = input()
        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Welcome ' + user)
        self.screen.printScreen()
        sleep(3)
        return user
    
    
    def loadingScreen(self):
        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Get ready...')
        self.screen.printScreen()
        sleep(5)
 


    def startGame(self):
        while self.listener.running:            
            self.screen.clearScreen()
            self.screen.drawFrame()
            self.mainPlayer.drawElement(self.screen)
            self.displayLife()
            self.displayDifficulty(1)
            self.screen.printScreen()
            sleep(0.1)
            self.mainPlayer.nextFrame(self.screen)

    def exitGame(self):
        self.screen.drawFrame()
        self.screen.drawStringAt(10, 4, 'Good Bye, from GAME PY')
        self.screen.printScreen()
        


    def displayDifficulty(self, level: int):
        if (level == game_levels.EASY):
            self.screen.drawStringAt(3, 2, 'Difficulty: EASY')
        elif (level == game_levels.MODERATE):
            self.screen.drawStringAt(3, 2, 'Difficulty: MODERATE')
        elif (level == game_levels.HARD):
            self.screen.drawStringAt(3, 2, 'Difficulty: HARD')
