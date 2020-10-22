  
from bibliopixel.animation.cube import Cube

class Laser(Cube):

    def __init__(self, layout, color=(255,255,255), speed=1, **kwds):
        super().__init__(layout, **kwds)
        self._color = color
        self._speed = speed

    def step(self, amt=1):
        if (self._step % self._speed) == 0:
            self.layout.all_off()
            iteration = (self._step // self._speed)
            traveling_up = (iteration // self.z) % 2 == 0
            for x in range(self.x):
                for y in range(self.y):
                    self.layout.set(x, y, (iteration % self.z) if traveling_up else ((self.z - 1) if ((iteration % self.z) == 0) else 0), self._color)
        self._step = self._step + 1