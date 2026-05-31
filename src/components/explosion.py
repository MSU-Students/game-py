from src.components.animation_frame import AnimationFrame
from src.components.element import Element

class Explosion(Element, AnimationFrame):

    alive = True

    def __init__(self):

        Element.__init__(self, [[]])

        self.loadAnimation('./animations/explosion.txt')

        self._current_frame = self.getAnimationFrame()

    def nextFrame(self):

        frame = self.getAnimationFrame()

        if frame == False:
            self.alive = False
        else:
            self._current_frame = frame

    def getFrame(self):

        if not self.alive:
            return False

        return (
            self._position[0],
            self._position[1],
            self._current_frame
        )