from abc import abstractmethod, ABC
from pynput import keyboard
from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.enemy_player import EnemyPlayer
from src.components.player import AirPlane, BasePlayer
import src.modules.game_levels as game_levels
from src.modules.game_levels import GameLevels
from src.components.waves import Waves
from ..utils import TimeClass

class GameNavigation(ABC):
    timeClass = TimeClass()
    screen: Screen
    mainPlayer: AirPlane
    enemies: list[EnemyPlayer]
    listener: keyboard.Listener
    waves: Waves
    paused: bool
    pauseMessage: str
    gameLevels: GameLevels
    save_folder = "./save_data"
    
    def __init__(self):
        self.allowDisplayNextWave: bool = False
        self.paused = False
        self.pauseMessage = ''
    def welcomeScreen(self):
        self.screen.drawStringAt(31, 17, 'Welcome to GAME PY')
        self.screen.printScreen()
        sleep(3)

    def resetScreen(self):
        self.screen.clearScreen()
        self.screen.drawFrame()

    def displayLife(self): #This will display the Health of the player while playing
        self.screen.drawStringAt(65 , 32, f'life: {str(self.mainPlayer.life)}')
    
    def displayKillCount(self): #This will display the killCount while playing
        self.screen.drawStringAt(65 , 30, f'kills: {str(self.waves.killCount)}')

    def profileInput(self):
        self.resetScreen()
        self.screen.drawStringAt(32, 17, 'Enter Your Name:')
        self.screen.printScreen()
        goto_xy((33, 19))
        user = input().strip()
        
        # NEW: Check if profile exists
        if self.has_existing_profile(user):
            self.resetScreen()
            self.screen.drawStringAt(25, 17, 'Profile found!')
            self.screen.drawStringAt(20, 19, '1. Continue Saved Game')
            self.screen.drawStringAt(20, 21, '2. Start New Game')
            self.screen.printScreen()
            goto_xy((20, 23))
            choice = input().strip()
            
            if choice == '1':
                saved_data = self.load_profile(user)
                if saved_data:
                    self.mainPlayer.first_name = saved_data['player_name']
                    self.mainPlayer.setRemainingLife(saved_data['current_life'])
                    self.mainPlayer.kill = saved_data['kill_count']
                    self.waves.currentWave = saved_data['current_wave']
                    self.gameLevels.currentDifficulty = saved_data['difficulty']
                    
                    self.resetScreen()
                    self.screen.drawStringAt(28, 17, f'Welcome back, {user}!')
                    self.screen.drawStringAt(25, 19, f'Wave: {saved_data["current_wave"]}, Life: {saved_data["current_life"]}')
                    self.screen.printScreen()
                    sleep(3)
                    return user
           
        
        self.resetScreen()
        self.screen.drawStringAt(33, 17, 'Welcome ' + user)
        self.screen.printScreen()
        sleep(3)
        return user
    
    def chooseDifficulty(self):
        difficultyInput: str = '0' # Default value, will be changed.
        difficultyString: str = ' ' # This will display the difficulty
        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Choose Difficulty (1-EASY, 2-MODERATE, 3-HARD): ')
        self.screen.printScreen()
        goto_xy((3, 12))
        difficultyInput = input()
        while difficultyInput not in ['1', '2', '3']:
            self.resetScreen()
            self.screen.drawStringAt(3, 10, 'Invalid input...')
            self.screen.printScreen()
            sleep(1)
            self.resetScreen()
            self.screen.drawStringAt(3, 10, 'Choose Difficulty (1-EASY, 2-MODERATE, 3-HARD): ')
            self.screen.printScreen()
            goto_xy((3, 12))
            difficultyInput = input()
            
        # /////////////////////////////////////////////////////////////////////////////
        if difficultyInput == '1':
            self.gameLevels.currentDifficulty = game_levels.EASY
            difficultyString = 'EASY'
        elif difficultyInput == '2':
            self.gameLevels.currentDifficulty = game_levels.MODERATE
            difficultyString = 'MODERATE'
        elif difficultyInput == '3':
            self.gameLevels.currentDifficulty = game_levels.HARD
            difficultyString = 'HARD'
        # /////////////////////////////////////////////////////////////////////////////

        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Chosen difficulty: ' + difficultyString)
        self.screen.printScreen()
        sleep(3)
    
    def loadingScreen(self):
        self.resetScreen()
        self.blinkText("READY?", 37, 17, 3)
        self.screen.drawStringAt(34, 17, 'Get ready...')
        self.screen.printScreen()
        sleep(1)
 
    def blinkText(self, text = "READY?", x=37, y=17, times=3):
        for i in range(times):
            #show the text
            self.screen.clearScreen()
            self.screen.drawFrame();
            self.screen.drawStringAt(x, y, text)
            self.screen.printScreen()
            sleep(0.5)
            #hide the text
            self.screen.clearScreen()
            self.screen.drawFrame();
            self.screen.printScreen()
            sleep(0.5)

    @abstractmethod
    def beforeNextFrame(self):
        pass
    
    @abstractmethod
    def afterNextFrame(self):
        pass
    
    def displayNextWave(self): # After all enemies are unalived, display the next wave.
        self.timeClass.timeCheck()
        if len(self.enemies) == 0 and self.allowDisplayNextWave == False:
            self.allowDisplayNextWave = True
        if self.allowDisplayNextWave == True:
            self.timeClass.startTimer(3.0)
            self.timeClass.timerFinished()
            if self.timeClass.timerFinished() != True:
                self.screen.drawStringAt(32, 15, f"Wave Number: {self.waves.currentWave}")
            else:
                self.allowDisplayNextWave = False

    def startGame(self):
        while self.listener.running:     
            self.screen.clearScreen()
            self.screen.drawFrame()

            if self.paused:
                self.screen.drawStringAt(32, 17, 'PAUSED - Press P')
                if (self.pauseMessage != ''):
                    self.screen.drawStringAt(32, 19, f'Something went wrong: {self.pauseMessage}')
            else:
                self.beforeNextFrame()
                player : BasePlayer   
                for player in self:
                    player.drawElement(self.screen)
                    player.nextFrame(self.screen)
                    
                self.afterNextFrame()

            if (self.waves.waveChanged == True): # After a wave is complete, configure another wave of enemies.
                if (self.timeClass.timerFinished() == True): # References of self.timeClass methods are in the displayNextWave().
                    self.gameLevels.spawnGameBasedOnDiff(self)       

            self.displayLife()
            self.displayKillCount()
            self.displayDifficulty(1)
            self.displayNextWave()
            self.screen.printScreen()
            self.waves.nextWave()
            sleep(0.1)
                


    def exitGame(self):
        self.screen.drawFrame()
        self.screen.drawStringAt(29, 17, 'Good Bye, from GAME PY')
        self.screen.printScreen()
    

    def displayDifficulty(self, level: int):
        if (level == game_levels.EASY):
            self.screen.drawStringAt(3, 32, 'Difficulty: EASY')
        elif (level == game_levels.MODERATE):
            self.screen.drawStringAt(3, 32, 'Difficulty: MODERATE')
        elif (level == game_levels.HARD):
            self.screen.drawStringAt(3, 32, 'Difficulty: HARD')
    
    def get_save_path(self, player_name: str):
        import os
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
        return os.path.join(self.save_folder, f"{player_name}.json")

    def save_profile(self, player_name: str, current_wave: int, current_life: int, 
                    kill_count: int, difficulty: int):
        import json
        save_data = {
            "player_name": player_name,
            "current_wave": current_wave,
            "current_life": current_life,
            "kill_count": kill_count,
            "difficulty": difficulty
        }
        
        save_path = self.get_save_path(player_name)
        
        try:
            with open(save_path, "w") as f:
                json.dump(save_data, f, indent=4)
            print(f"\n✓ Game saved for {player_name}!")
            return True
        except Exception as e:
            print(f"\n✗ Error saving game: {e}")
            return False

    def load_profile(self, player_name: str):
        import json
        import os
        save_path = self.get_save_path(player_name)
        
        if not os.path.exists(save_path):
            return None
        
        try:
            with open(save_path, "r") as f:
                save_data = json.load(f)
            return save_data
        except Exception as e:
            print(f"\n✗ Error loading game: {e}")
            return None

    def has_existing_profile(self, player_name: str):
        import os
        save_path = self.get_save_path(player_name)
        return os.path.exists(save_path)

    def saveCurrentGame(self):
        self.save_profile(
            self.mainPlayer.first_name,
            self.waves.currentWave,
            self.mainPlayer.life,
            self.mainPlayer.kill,
            self.gameLevels.currentDifficulty
        )

    def mainMenu(self):
        self.resetScreen()
        self.screen.drawStringAt(28, 10, '=== MAIN MENU ===')
        self.screen.drawStringAt(25, 14, '1. New Game')
        self.screen.drawStringAt(25, 16, '2. Continue Saved Game')
        self.screen.printScreen()
        goto_xy((25, 18))
        choice = input().strip()
        
        if choice == '2':
            self.resetScreen()
            self.screen.drawStringAt(28, 10, '=== SAVED GAMES ===')
            
            import os
            if not os.path.exists(self.save_folder):
                os.makedirs(self.save_folder)
            
            saved_files = [f.replace('.json', '') for f in os.listdir(self.save_folder) if f.endswith('.json')]
            
            if not saved_files:
                self.screen.drawStringAt(25, 14, 'No saved games found!')
                self.screen.printScreen()
                sleep(2)
                return self.mainMenu()  
            
            y_pos = 14
            for i, save_name in enumerate(saved_files):
                self.screen.drawStringAt(25, y_pos, f'{i+1}. {save_name}')
                y_pos += 1
            
            self.screen.printScreen()
            goto_xy((25, y_pos + 1))
            choice = input().strip()
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(saved_files):
                    selected_name = saved_files[idx]
                    saved_data = self.load_profile(selected_name)
                    if saved_data:
                        self.mainPlayer.first_name = saved_data['player_name']
                        self.mainPlayer.setRemainingLife(saved_data['current_life'])
                        self.mainPlayer.kill = saved_data['kill_count']
                        self.waves.currentWave = saved_data['current_wave']
                        self.gameLevels.currentDifficulty = saved_data['difficulty']
                        
                        self.resetScreen()
                        self.screen.drawStringAt(28, 14, f'Welcome back, {selected_name}!')
                        self.screen.drawStringAt(25, 16, f'Wave: {saved_data["current_wave"]}, Life: {saved_data["current_life"]}')
                        self.screen.printScreen()
                        sleep(3)
                        return selected_name
            except:
                pass
        
        return None
