from pynput import keyboard
from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.player import AirPlane
from src.components.enemy_player import EnemyPlayer
from src.components.waves import Waves

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

