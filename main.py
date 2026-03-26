from player import Player
from utils import clear_console

player = Player('Luffy', 'D')
clear_console()
player.setPosition((20, 20))
player.display()
player.setPosition((8, 15))
player.display()