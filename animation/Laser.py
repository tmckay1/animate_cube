  
from bibliopixel.animation.cube import Cube

class Laser(Cube):

    def __init__(self, layout, color=(255,255,255), speed=1, **kwds):
        super().__init__(layout, **kwds)
        self._color = color
        self._speed = speed

    def step(self, amt=8):
        if (self._step % self._speed) == 0:
            self.layout.all_off()
            for x in range(self.x):
                for y in range(self.y):
                    self.layout.set(x, y, self._step % self.z, (255,0,0))
        self._step = self._step + 1