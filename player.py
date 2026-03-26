from utils import clear_console, goto_xy
class Player:
    # Constructor
    def __init__(self, fName = '', lName = ''):
        self.first_name = fName
        self.last_name = lName
        self.__position = (0, 0)
        self.__age = 0

    def fullName(self, separator = ' '):
        return f'{self.first_name}{separator}{self.last_name}'

    def setPosition(self, position):
        self.__position = (position[0], position[1])

    def display(self):
        goto_xy(self.__position)
        print(self.fullName())

