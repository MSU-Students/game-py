from src.components.player import BasePlayer
from src.components.element import Element

class DescendingEnemy(BasePlayer):
    life = 1
    alive = True

    def __init__(self, fName='', lName='', pixels=None):
        super().__init__(fName, lName)
        if pixels is None:
            pixels = [
                ['M','M','M'],
                ['M','M','M']
            ]
        try:
            self._Element__pixels = pixels
        except Exception:
            try:
                Element.__init__(self, pixels)
            except Exception:
                pass

    def getType(self):
        return 'DescendingEnemy'

    def fullName(self, separator=' '):
        return f'[DescendingEnemy] {self.first_name}{separator}{self.last_name}'

    def is_alive(self):
        return getattr(self, 'alive', True)

    def decrementLife(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.alive = False

    def getFrame(self):
        if not self.is_alive():
            return False
        pixels = getattr(self, '_Element__pixels', None)
        if pixels is None:
            return super().getFrame()
        return (self._position[0], self._position[1], pixels)

    def nextFrame(self, screen):
        if not self.is_alive():
            return
        self.movePosition((0, 1))

    def getCoveredCoords(self):
        pixels = getattr(self, '_Element__pixels', None)
        if pixels is None:
            f = super().getFrame()
            if not f:
                return set()
            x, y, pixels = f
        x, y = self._position
        coords = set()
        for ry, row in enumerate(pixels):
            for rx, ch in enumerate(row):
                if ch != ' ':
                    coords.add((x + rx, y + ry))
        return coords
