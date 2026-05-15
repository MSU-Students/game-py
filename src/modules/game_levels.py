from src.components.enemy_player import EnemyPlayer
from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.player import AirPlane
from pynput import keyboard

EASY, MODERATE, HARD = 1, 2, 3
currentDifficulty = EASY # Default difficulty is easy, will be changed once the user inputs other difficulty
# Point System and Game Mechanics
class GameLevels:
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener

    def setupGame(self):
        if (currentDifficulty == EASY):
            self.mainPlayer.setRemainingLife(10)
            pass
        elif (currentDifficulty == MODERATE):
            pass
        elif (currentDifficulty == HARD):
            pass
    
    def checkCollisions(self):
        self.mainPlayer.checkIfColliding(self.enemies)
        for enemy in self.enemies:
            enemy.checkIfColliding([self.mainPlayer])
    
    def eliminateDeads(self):
        for enemy in self.enemies:
            if (not enemy.is_alive()):
                self.enemies.remove(enemy)