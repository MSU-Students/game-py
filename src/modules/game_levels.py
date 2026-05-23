from src.components.enemy_player import EnemyPlayer
from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.player import AirPlane
from pynput import keyboard
from src.components.waves import Waves

EASY, MODERATE, HARD = 1, 2, 3

# Point System and Game Mechanics
class GameLevels:
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener
    waves: Waves
    currentDifficulty = EASY # Default difficulty is easy, will be changed once the user inputs other difficulty
    
    def setupGame(self): # Initial only.
        if (self.currentDifficulty == EASY):
            self.mainPlayer.setRemainingLife(10)
        elif (self.currentDifficulty == MODERATE):
            self.mainPlayer.setRemainingLife(15)
        elif (self.currentDifficulty == HARD):
            self.mainPlayer.setRemainingLife(20)
    
    def spawnGameBasedOnDiff(self): # Initial and Post-initial.
        if (self.currentDifficulty == EASY):
            self.waves.waveSpawnEnemiesOnEasy()
        elif (self.currentDifficulty == MODERATE):
            self.waves.waveSpawnEnemiesOnModerate()
        elif (self.currentDifficulty == HARD):
            self.waves.waveSpawnEnemiesOnHard()
    
    def checkCollisions(self):
        self.mainPlayer.checkIfColliding(self.enemies)
        for enemy in self.enemies:
            enemy.checkIfColliding([self.mainPlayer])
    
    def eliminateDeads(self):
        for enemy in self.enemies:
            if (not enemy.is_alive()):
                self.enemies.remove(enemy)
                self.waves.killCount += 1