from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane
from enemy_player import EnemyPlayer
from pynput import keyboard
from waves import Waves
class GameStory:
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener
    waves: Waves

    def loadMainPlayer(self, name: str):
        self.mainPlayer.first_name = name
        (width, height) = self.screen.getDimension()
        self.mainPlayer.setPosition((int(width / 2), height - 8))
    def loadEnemies(self):
        self.waves.loadEnemyPos(5)
    
