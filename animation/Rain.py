import random
from bibliopixel.colors.arithmetic import color_scale
from bibliopixel.animation.cube import Cube

class Rain(Cube):

  def __init__(self, layout, tail=4, growthRate=12, speed = 1, **kwds):
    super().__init__(layout, **kwds)
    self._tail = tail
    self._speed = speed
    self._drops = [[[] for y in range(self.y)] for x in range(self.x)]
    self._growthRate = growthRate

  def pre_run(self):
    self._step = 0

  def _drawDrop(self, x, y, z, color):
    for i in range(self._tail):
      if z + i >= 0 and z + i < self.z:
        level = 255 - ((255 // self._tail) * i)
        self.layout.set(x, y, z + i, (0,255,0))

  def step(self, amt=1):
    if self._step % self._speed == 0:
        self.layout.all_off()

        for i in range(self._growthRate):
          x = random.randint(0, self.x - 1)
          y = random.randint(0, self.y - 1)
          self._drops[x][y].append(0)

        for x in range(self.x):
          for y in range(self.y):
            col = self._drops[x][y]
            if len(col) > 0:
              removals = []
              for z in range(len(col)):
                drop = col[z]
                if drop < self.y:
                  self._drawDrop(x, y, drop, self.palette(
                    drop * (255 // self.z)))
                if drop - (self._tail - 1) < self.z:
                  drop = drop + 1
                  self._drops[x][y][z] = drop
                else:
                  removals.append(drop)
              for r in removals:
                self._drops[x][y].remove(r)

    self._step = self._step + 1