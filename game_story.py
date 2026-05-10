from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane, EnemyPlayer
from pynput import keyboard
from waves import Waves
class GameStory:
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener
    wave: Waves

    def loadMainPlayer(self, name: str):
        self.mainPlayer.first_name = name
        (width, height) = self.screen.getDimension()
        self.mainPlayer.setPosition((int(width / 2), height - 8))
    def loadEnemies(self):
        self.wave.loadEnemyPos(5)
    
