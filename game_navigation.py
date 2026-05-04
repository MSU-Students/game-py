from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane
from pynput import keyboard
class GameNavigation:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener
    def welcomeScreen(self):
        self.screen.drawStringAt(3, 10, 'Welcome to GAME PY')
        self.screen.printScreen()
        sleep(3)

    def resetScreen(self):
        self.screen.clearScreen()
        self.screen.drawFrame()

    def profileInput(self):
        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Enter Your Name:')
        self.screen.printScreen()
        goto_xy((3, 12))
        user = input()
        self.resetScreen()
        self.screen.drawStringAt(3, 10, 'Welcome ' + user)
        self.screen.printScreen()
        sleep(3)
        return user
    
    def startGame(self):
        while self.listener.running:            
            self.screen.clearScreen()
            self.screen.drawFrame()
            # draw main player
            self.mainPlayer.drawElement(self.screen)
            # draw enemies
            for enemy in list(self.enemies):
                if hasattr(enemy, 'is_alive') and not enemy.is_alive():
                    try:
                        self.enemies.remove(enemy)
                    except ValueError:
                        pass
                    # spawn replacement
                    if hasattr(self, 'spawn_enemy'):
                        try:
                            self.spawn_enemy()
                        except Exception:
                            pass
                    continue
                enemy.drawElement(self.screen)
            # draw amos and advance frames
            for amo in list(self.mainPlayer.amos):
                if not getattr(amo, 'alive', True):
                    try:
                        self.mainPlayer.amos.remove(amo)
                    except ValueError:
                        pass
                    continue
                amo.drawElement(self.screen)
            self.screen.printScreen()
            sleep(0.1)
            # advance frames
            self.mainPlayer.nextFrame(self.screen)
            for enemy in list(self.enemies):
                enemy.nextFrame(self.screen)
            # collision detection between amos and enemies
            for amo in list(self.mainPlayer.amos):
                if not getattr(amo, 'alive', True):
                    continue
                ax, ay = amo._position
                for enemy in list(self.enemies):
                    if not hasattr(enemy, 'get_hit_coords'):
                        continue
                    if (ax, ay) in enemy.get_hit_coords():
                        enemy.decrementLife()
                        amo.alive = False
                        try:
                            self.mainPlayer.amos.remove(amo)
                        except ValueError:
                            pass
                        if hasattr(enemy, 'is_alive') and not enemy.is_alive():
                            try:
                                self.enemies.remove(enemy)
                            except ValueError:
                                pass
                            # spawn replacement enemy
                            if hasattr(self, 'spawn_enemy'):
                                try:
                                    self.spawn_enemy()
                                except Exception:
                                    pass
                        break

    def exitGame(self):
        self.screen.drawFrame()
        self.screen.drawStringAt(10, 4, 'Good Bye, from GAME PY')
        self.screen.printScreen()