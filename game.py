from player import MainPlayer, EnemyPlayer
# How to make a Class Iterable
# 1: declare index
# 2: override __iter__, returns self
# 3: override __next__, return present based from __index prop
# 4: increment self.__index
# 5: stop iteration, by raise StopIteration
class Game:
    __index = 0 # step 1
    def __init__(self, firstName, lastName):
        self.mainPlayer = MainPlayer(firstName, lastName)
        self.enemies = [
            EnemyPlayer('Black', 'Bird'),
            EnemyPlayer('Enel', 'God')
        ]
    # called every start of iteration
    def __iter__(self): #step 2
        self.__index = 0
        return self
    
    def __next__(self):#step 3
        if self.__index == 0:
            self.__index += 1
            return self.mainPlayer
        elif self.__index <= self.enemies.__len__():
            self.__index += 1
            return self.enemies[self.__index - 2]
        else:
            raise StopIteration #step 4