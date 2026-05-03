from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane, EnemyPlayer
from pynput import keyboard
class GameStory:
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener

    def loadMainPlayer(self, name: str):
        self.mainPlayer.first_name = name
        (width, height) = self.screen.getDimension()
        self.mainPlayer.setPosition((int(width / 2), height - 8))
    def loadEnemies(self):
        (width, height) = self.screen.getDimension()
        for enemy in range(len(self.enemies)):
            if enemy==0:
                self.enemies[enemy].setPosition((4, 10))
            elif enemy==1:
                self.enemies[enemy].setPosition((int((width/2)-3), 2))
            elif enemy==2:
                self.enemies[enemy].setPosition((int(width - 15), 2))
