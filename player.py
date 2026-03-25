class Player:
    # Constructor
    def __init__(self, fName = '', lName = ''):
        self.first_name = fName
        self.last_name = lName
        self.__position = 'Member'
        self.__age = 0

    def fullName(self, separator = ' '):
        return f'{self.first_name}{separator}{self.last_name}'

    def setPosition(self, position: str):
        self.__position = position
