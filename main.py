from utils import clear_console
from game import Game

try:
    myGame = Game('0', 'Hat')

    for player in myGame:
        print(f' {player.fullName()}')

    number = 123
    y = 1
    x = number / y

    print(x)
except ZeroDivisionError:
    print(f'Division error numerator {number} and denominator {y}')
except Exception as err:
    
    print(f'Something went wrong: {err}')
finally:
    print('After execution')
