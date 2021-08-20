  
from bibliopixel.animation.cube import Cube

class Laser(Cube):

    def __init__(self, layout, color=(255,255,255), **kwds):
        super().__init__(layout, **kwds)
        self._color = color

    def step(self, amt=1):
        self.layout.all_off()
        new_step = self._step
        traveling_up = (new_step // self.z) % 2 == 0
        for x in range(self.x):
            for y in range(self.y):
                self.layout.set(x, y, (new_step % self.z) if traveling_up else (self.z - (new_step % self.z) - 1), self._color)

        # TODO: Handle overflow
        self._step += amt