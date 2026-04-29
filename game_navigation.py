from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane
from pynput import keyboard
class GameNavigation:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener
    def __init__(self):
        self.paused = False
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
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        while True:        
            self.screen.clearScreen()
            self.screen.drawFrame()

            if self.paused:
                self.screen.drawStringAt(10, 5, 'PAUSED - Press P')
            else:
                self.mainPlayer.drawElement(self.screen)
                self.mainPlayer.nextFrame(self.screen)

            self.screen.printScreen()
            sleep(0.1)
                

    def exitGame(self):
        self.screen.drawFrame()
        self.screen.drawStringAt(10, 4, 'Good Bye, from GAME PY')
        self.screen.printScreen()
    
    def on_press(self, key):
        try:
            if key.char == 'p':
                self.paused = not self.paused 
                print (f"Paused status: {self.paused}")

        except AttributeError:

            pass
        