from src.components.enemy_player import Enemy03, EnemyPlayer
from src.core.screen import Screen

# Waves.py is all about waves and anything that relates to it such as enemy number, etc.

WAVEONE, WAVETWO, WAVETHREE, WAVEFOUR, WAVEFIVE = 1, 2, 3, 4, 5
class Waves:
    screen:Screen
    def __init__(self, gameScreen:Screen):
        self.waveChanged: bool = False # This variable prevents from changing of the wave number indefinitely.
        self.currentWave: int = WAVEONE
        self.screen = gameScreen
        self.enemy: EnemyPlayer
        self.enemies: list[EnemyPlayer] = []
        self.distancer: int # This is the distance between enemies once the game started
        self.count: int
        (self.width, self.height) = self.screen.getDimension()

    # Creates enemies (that are not bosses), pass it to some integer, it will instance that number of enemies
    def instantiateEnemies(self, enemyNumberGetter: int):
        self.enemies.clear() # Ensures that any overwritten data before this is cleared.
        for i in range(enemyNumberGetter):
            self.enemy = EnemyPlayer()
            self.enemies.append(self.enemy)

    # Used to load enemies', pass it to some integer to spawn that number of enemies once the main game started
    # It is also used for the initial position of the enemies.
    def loadEnemyPos(self, enemyNumberGetter: int):
        self.instantiateEnemies(enemyNumberGetter)

        if enemyNumberGetter == 5:
            #If number of enemies is five, form in one horizontal line
            self.distancer = self.width / 5
            for enemy in range(enemyNumberGetter):
                self.count = enemy + 1
                self.enemies[enemy].setPosition((int(self.distancer * self.count) - 11, 2))
        
        elif enemyNumberGetter > 5 and enemyNumberGetter <= 10:
            # If number of enemies is more than five and less than 11, form in two horizontal lines
            self.distancer = self.width / 5
            for enemy in range(enemyNumberGetter):
                if enemy <= 4: # Line of enemies number 1
                    self.count = enemy + 1
                    self.enemies[enemy].setPosition((int(self.distancer * self.count) - 11, 2))
                if enemy > 4: # Line of enemies number 2
                    self.count = enemy - 4
                    self.enemies[enemy].setPosition((int(self.distancer * self.count) - 11, 6))
        
        elif enemyNumberGetter > 10 and enemyNumberGetter <= 15:
            # If number of enemies is more than ten and less than 16, form in three horizontal lines
            self.distancer = self.width / 5
            for enemy in range(enemyNumberGetter):
                if enemy <= 4: # Line of enemies number 1
                    self.count = enemy + 1
                    self.enemies[enemy].setPosition((int(self.distancer * self.count) - 11, 2))
                if enemy > 4 and enemy <= 9 : # Line of enemies number 2
                    self.count = enemy - 4
                    self.enemies[enemy].setPosition((int(self.distancer * self.count) - 11, 6))
                if enemy > 9: # Line of enemies number 3
                    self.count = enemy - 9
                    self.enemies[enemy].setPosition((int(self.distancer * self.count) - 11, 10))
    
        elif enemyNumberGetter > 15 and enemyNumberGetter <= 30:
            # If number of enemies is more than fifteen and less than 31, form in three horizontal lines
            self.distancer = self.width / 11
            for enemy in range(enemyNumberGetter):
                if enemy <= 9: # Line of enemies number 1
                    self.count = enemy + 1
                    self.enemies[enemy].setPosition((int(self.distancer * self.count) - 2, 2))
                if enemy > 9 and enemy <= 19 : # Line of enemies number 2
                    self.count = enemy - 9
                    self.enemies[enemy].setPosition((int(self.distancer * self.count) - 2, 6))
                if enemy > 19: # Line of enemies number 3
                    self.count = enemy - 19
                    self.enemies[enemy].setPosition((int(self.distancer * self.count) - 2, 10))    

    def setEnemiesStatus(self, life: int, moveSpeed: int):
        for enemy in range(len(self.enemies)):
            self.enemies[enemy].setRemainingLife(life)
            self.enemies[enemy].setMoveSpeed(moveSpeed)
                
    def waveSpawnEnemiesOnEasy(self):
        """Creates a number of enemies according to the current wave and easy difficulty"""
        if self.currentWave == WAVEONE:
            self.loadEnemyPos(5)
        elif self.currentWave == WAVETWO:
            self.loadEnemyPos(9)
        elif self.currentWave == WAVETHREE:
            self.loadEnemyPos(5)
        elif self.currentWave == WAVEFOUR:
            self.loadEnemyPos(15)
        elif self.currentWave == WAVEFIVE:
            self.loadEnemyPos(10)
        self.setEnemiesStatus(3, 1)

    
    def waveSpawnEnemiesOnModerate(self):
        """Creates a number of enemies according to the current wave and moderate difficulty"""
        if self.currentWave == WAVEONE:
            self.loadEnemyPos(10)
        elif self.currentWave == WAVETWO:
            self.loadEnemyPos(15)
        elif self.currentWave == WAVETHREE:
            self.loadEnemyPos(15)
        elif self.currentWave == WAVEFOUR:
            self.loadEnemyPos(18)
        elif self.currentWave == WAVEFIVE:
            self.loadEnemyPos(20)
        self.setEnemiesStatus(5, 1)

    def waveSpawnEnemiesOnHard(self):
        """Creates a number of enemies according to the current wave and hard difficulty"""
        if self.currentWave == WAVEONE:
            self.loadEnemyPos(20)
        elif self.currentWave == WAVETWO:
            self.loadEnemyPos(25)
        elif self.currentWave == WAVETHREE:
            self.loadEnemyPos(20)
        elif self.currentWave == WAVEFOUR:
            self.loadEnemyPos(30)
        elif self.currentWave == WAVEFIVE:
            self.loadEnemyPos(25)
        self.setEnemiesStatus(8, 2)


    def nextWave(self): # After all enemies are unalived, proceed to the next wave
        if len(self.enemies) == 0 and self.waveChanged == False:
            self.currentWave += 1
            self.waveChanged = True
        
        if len(self.enemies) > 0:
            self.waveChanged = False



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

