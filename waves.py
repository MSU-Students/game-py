import game_levels
from player import EnemyPlayer
from screen import Screen

# Waves.py is all about waves and anything that relates to it such as enemy number, etc.

WAVEONE, WAVETWO, WAVETHREE, WAVEFOUR, WAVEFIVE = 1, 2, 3, 4, 5
class Waves:
    screen = Screen()
    def __init__(self):
        self.enemy: EnemyPlayer
        self.enemies: list[EnemyPlayer] = []
        self.distancer: int # This is the distance between enemies once the game started
        self.count: int
        (self.width, self.height) = self.screen.getDimension()

    # Creates enemies (that are not bosses), pass it to some integer, it will spawn that number of enemies
    def instantiateEnemies(self, enemyNumberGetter: int):
        for i in range(enemyNumberGetter):
            self.enemy = EnemyPlayer()
            self.enemies.append(self.enemy)

    # Used to load enemies' position once the main game started
    def loadEnemyPos(self, enemyNumberGetter: int):
        self.instantiateEnemies(enemyNumberGetter)

        if enemyNumberGetter == 5:
            self.distancer = self.width / 5
            for enemy in range(enemyNumberGetter):
                self.count = enemy + 1
                self.enemies[enemy].setPosition((int(self.distancer * self.count) - 11, 2))

