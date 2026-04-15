from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane
from pynput import keyboard

EASY, MODERATE, HARD = 1, 2, 3
# Point System and Game Mechanics
class GameLevels:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener

    def setupGame(self, level: int):
        if (level == EASY):
            self.mainPlayer.setRemainingLife(5)
            pass
        elif (level == MODERATE):
            pass
        elif (level == HARD):
            pass