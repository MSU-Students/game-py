from animation_frame import AnimationFrame
from player import BasePlayer, STEADY, GOING_LEFT, GOING_RIGHT
from element import Element

class EnemyPlayer(BasePlayer):
    life = 100
    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        self._avatar = '[*]'
    def decrementLife(self):
        self.life = self.life - 1
    def getType(self):
        return 'Enemy'
    def fullName(self, separator=' '):
        return f'[Enemy] {super().fullName(separator)}'

class Enemy03(BasePlayer, AnimationFrame):
    life = 1
    alive = True
    _current_frame = None

    def __init__(self, fName='', lName=''):
        super().__init__(fName, lName)
        self._avatar = '[E3]'
        self.loadAnimation('./animations/enemy03.txt')
        try:
            self.setState(0)
        except Exception:
            pass
        if hasattr(self, 'peekAnimationFrame'):
            self._current_frame = self.peekAnimationFrame()
        else:
            f = self.getAnimationFrame()
            if f:
                self._current_frame = f
                try:
                    self.setState(0)
                except Exception:
                    pass

    def decrementLife(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.alive = False

    def is_alive(self):
        return getattr(self, 'alive', True)

    def getType(self):
        return 'Enemy03'

    def fullName(self, separator=' '):
        return f'[Enemy03] {super().fullName(separator)}'

    def nextFrame(self, screen):
        if not self.is_alive():
            return
        frame = self.getAnimationFrame()
        if frame == False:
            try:
                self.setState(0)
            except Exception:
                pass
            frame = self.getAnimationFrame()
        if frame:
            self._current_frame = frame
        self.movePosition((0, 1))

    def getFrame(self):
        if not self.is_alive():
            return False
        if self._current_frame is None:
            if hasattr(self, 'peekAnimationFrame'):
                self._current_frame = self.peekAnimationFrame()
        return (self._position[0], self._position[1], self._current_frame if self._current_frame is not None else [[]])

    def get_hit_coords(self):
        pixels = self._current_frame
        if pixels is None:
            if hasattr(self, 'peekAnimationFrame'):
                pixels = self.peekAnimationFrame()
        if not pixels:
            return set()
        x, y = self._position
        coords = set()
        for ry, row in enumerate(pixels):
            for rx, ch in enumerate(row):
                if ch != ' ':
                    coords.add((x + rx, y + ry))
        return coords


class DescendingEnemy(BasePlayer):
    """An enemy that starts at the top and descends one row per frame. Dies in one hit."""
    life = 1
    alive = True

    def __init__(self, fName='', lName='', pixels=None):
        # initialize BasePlayer fields
        super().__init__(fName, lName)
        # override sprite pixels
        if pixels is None:
            pixels = [
                [' ', 'V', ' '],
                ['/', '|', '\\']
            ]
        try:
            self._Element__pixels = pixels
        except Exception:
            # fallback: call Element.__init__ if available
            try:
                Element.__init__(self, pixels)
            except Exception:
                pass

    def getType(self):
        return 'DescendingEnemy'

    def is_alive(self):
        return getattr(self, 'alive', True)

    def decrementLife(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.alive = False

    def getFrame(self):
        if not self.is_alive():
            return False
        self.movePosition((0, 1))
        pixels = getattr(self, '_Element__pixels', None)
        if pixels is None:
            return super().getFrame()
        return (self._position[0], self._position[1], pixels)

    def get_hit_coords(self):
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

