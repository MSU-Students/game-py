from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane
from pynput import keyboard
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
    
    def startGame(self):
        while self.listener.running:            
            self.screen.clearScreen()
            self.screen.drawFrame()
            self.mainPlayer.drawElement(self.screen)
            self.screen.printScreen()
            sleep(0.1)
            self.mainPlayer.nextFrame(self.screen)

    def exitGame(self):
        self.screen.drawFrame()
        self.screen.drawStringAt(10, 4, 'Good Bye, from GAME PY')
        self.screen.printScreen()