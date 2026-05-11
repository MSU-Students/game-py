import src.modules.game_levels as game_levels
from src.components.enemy_player import Enemy03, EnemyPlayer
from src.core.screen import Screen

# Waves.py is all about waves and anything that relates to it such as enemy number, etc.

WAVEONE, WAVETWO, WAVETHREE, WAVEFOUR, WAVEFIVE = 1, 2, 3, 4, 5
class Waves:
    screen:Screen
    def __init__(self, gameScreen:Screen):
        self.screen = gameScreen
        self.enemy: EnemyPlayer
        self.enemies: list[EnemyPlayer] = []
        self.distancer: int # This is the distance between enemies once the game started
        self.count: int
        (self.width, self.height) = self.screen.getDimension()

    # Creates enemies (that are not bosses), pass it to some integer, it will spawn that number of enemies
    def instantiateEnemies(self, enemyNumberGetter: int):
        self.enemies.clear() # Ensures that any overwritten data before this is cleared.
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
                
    def spawn_enemy(self):
        spawnEnemies = list(filter(lambda enemy: isinstance(enemy, Enemy03), self.enemies))
        if (spawnEnemies.__len__() > 0):
            return
        """Create and position a new Enemy03 at the top-center of the screen."""
        e = Enemy03('Waving', 'Enemy')
        width, height = self.screen.getDimension()
        # try to center enemy (assume width of frame ~3); place at row 1
        e.setPosition((max(1, int(width / 2) - 1), 1))
        try:
            e.setState(0)
        except Exception:
            pass
        self.enemies.append(e)

