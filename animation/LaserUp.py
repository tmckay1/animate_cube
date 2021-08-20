  
from bibliopixel.animation.cube import Cube

class LaserUp(Cube):

    def __init__(self, layout, color=(255,255,255), **kwds):
        super().__init__(layout, **kwds)
        self._color = color

    def step(self, amt=1):
        self.layout.all_off()
        for x in range(self.x):
            for y in range(self.y):
                self.layout.set(x, y, (self._step // self._speed) % self.z, (255,0,0))
        self._step += amt