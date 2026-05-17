from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane
from pynput import keyboard
class GameStory:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener

    def loadMainPlayer(self, name: str):
        self.mainPlayer.first_name = name
        (width, height) = self.screen.getDimension()
        self.mainPlayer.setPosition((int(width / 2), height - 8))