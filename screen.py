from utils import clear_console
class Screen:
    __width = 80
    __height = 24
    __x = 0
    __y = 0
    __pixels = []
    def __init__(self, width = 0, height = 0):
        self.__width = width if width > 0 else self.__width
        self.__height = height if height > 0 else self.__height
        self.initFrame()
    def initFrame(self):
        self.clearScreen()
        self.drawFrame()
    def drawPixelsAt(self, pixels:list, x = 1, y = 1):
        cy = 0
        for row in pixels:
            cx = 0
            for col in row:
                ty = y + cy
                tx = x + cx
                if ty < self.__height and tx < self.__width:
                    self.__pixels[ty][tx] = col
                cx = cx + 1
            cy = cy + 1

    def drawStringAt(self, x = 1, y = 1, c = 'X'):
        self.__pixels[x][y] = c
    def clearScreen(self):
        self.__pixels = [[' ' for _ in range(self.__width)] for _ in range(self.__height)]
    
    def drawFrame(self):
        firsRow = self.__pixels[0]
        for i in range(0, self.__width):
            firsRow[i] = '='
        lastRow = self.__pixels[self.__height - 1]
        for i in range(0, self.__width):
            lastRow[i] = '='
        
        for y in range(1, self.__height - 1):
            row = self.__pixels[y]
            row[0] = '|'
            row[self.__width - 1] = '|'

    def printScreen(self):
        clear_console()
        #start 0,0
        for row in self.__pixels:
            for col in row:
                print(col, end='')
            print('')
