from functools import reduce

class AnimationFrame:
    __animations = [[[]]]
    __stateCount = 0
    __stateIndex = 0
    __frameIndex = 0
    def setState(self, state: int):
        self.__stateIndex = state
        self.__frameIndex = 0
    def getAnimationFrame(self):
        if (self.__animations.__len__() <= self.__stateIndex ):
            return False
        anime = self.__animations[self.__stateIndex]
        if (anime.__len__() <= self.__frameIndex):
            return False
        frame = self.__animations[self.__stateIndex][self.__frameIndex]
        self.__frameIndex += 1
        return frame
    
    def loadAnimation(self, path:str):
        def trimEndLine(line: str):
            return line.rstrip('\n') 
        def extractAnime(anime:list, line:str):
            if (line.startswith('===')):
                anime.append([[]])
                self.__stateCount += 1
            elif (line == '' Or line.startswith('---'):
                stateSize = anime.__len__()
                stateFrame = anime[stateSize -1]
                stateFrame.append([])
            else:
                stateSize = anime.__len__()
                stateFrame = anime[stateSize -1]
                animeSize = stateFrame.__len__()
                frame = stateFrame[animeSize - 1]
                frame.append(line)
            return anime
        with open(path, 'r') as file:
            lines = map(trimEndLine, file.readlines())
            self.__animations = reduce(extractAnime, lines, [[[]]])


# AirPlane (RIght - Going RIght), Left - Going Left