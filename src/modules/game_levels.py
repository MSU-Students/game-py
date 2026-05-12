from src.components.enemy_player import EnemyPlayer
from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.player import AirPlane
from pynput import keyboard

EASY, MODERATE, HARD = 1, 2, 3
# Point System and Game Mechanics
class GameLevels:
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener

    def setupGame(self, level: int):
        if (level == EASY):
            self.mainPlayer.setRemainingLife(5)
            pass
        elif (level == MODERATE):
            pass
        elif (level == HARD):
            pass
    
    def checkCollisions(self):
        self.mainPlayer.checkIfColliding(self.enemies)
        for enemy in self.enemies:
            enemy.checkIfColliding([self.mainPlayer])
    
    def eliminateDeads(self):
        for enemy in self.enemies:
            if (not enemy.is_alive()):
                self.enemies.remove(enemy)