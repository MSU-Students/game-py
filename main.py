from utils import clear_console
from game import Game


myGame = Game('Straw', 'Hat')

for player in myGame:
    print(f' {player.fullName()}')

