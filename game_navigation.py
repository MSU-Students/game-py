from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane, EnemyPlayer
from pynput import keyboard
import game_levels
from waves import Waves
class GameNavigation:
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener
    wave: Waves
    def welcomeScreen(self):
        self.screen.drawStringAt(3, 10, 'Welcome to GAME PY')
        self.screen.printScreen()
        sleep(3)

    def resetScreen(self):
        self.screen.clearScreen()
        self.screen.drawFrame()

    def displayLife(self): #This will display the Health of the player while playing
        self.screen.drawStringAt(65 , 32, f'life: {str(self.mainPlayer.life)}')

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
        self.screen.drawStringAt(33, 17, 'Get ready...')
        self.screen.printScreen()
        sleep(5)
 


    def startGame(self):
        while self.listener.running:     
            self.screen.clearScreen()
            self.screen.drawFrame()
            if self.paused:
                self.screen.drawStringAt(10, 5, 'PAUSED - Press P')
                if (self.pauseMessage != ''):
                    self.screen.drawStringAt(0, 10, f'Something went wrong: {self.pauseMessage}')
            else:
                self.mainPlayer.drawElement(self.screen)
                for enemy in self.enemies:
                    enemy.drawElement(self.screen)
                    enemy.moveEnemy(self.mainPlayer._position[0])
                    enemy.nextFrame(self.screen)
            
                print(self.enemies[0].enemyTimer.targetTime, '       ', self.enemies[2].enemyTimer.targetTime)
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
            self.screen.drawStringAt(3, 32, 'Difficulty: EASY')
        elif (level == game_levels.MODERATE):
            self.screen.drawStringAt(3, 32, 'Difficulty: MODERATE')
        elif (level == game_levels.HARD):
            self.screen.drawStringAt(3, 32, 'Difficulty: HARD')
