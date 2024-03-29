import random
from bibliopixel.colors.arithmetic import color_scale
from bibliopixel.animation.cube import Cube

class CubeRain(Cube):

  def __init__(self, layout, tail=4, growthRate=12, color = (0,0,0), clouds=False, **kwds):
    super().__init__(layout, **kwds)
    self._tail   = tail
    self._color  = color
    self._clouds = clouds
    self._drops  = [[[] for y in range(self.y)] for x in range(self.x)]
    self._growthRate = growthRate

  def pre_run(self):
    self._step = 0

  def _drawDrop(self, x, y, z):
    for i in range(self._tail):
      if z - i >= 0 and z - i < self.z:
        self.layout.set(x, y, z - i, self._color)

  def _drawClouds(self):
    white_color = (255,255,255)
    for x in range(self.x):
      for y in range(self.y):
        self.layout.set(x, y, self.z - 1, white_color)

  def step(self, amt=1):
    self.layout.all_off()

    if self._clouds:
      self._drawClouds()

    for i in range(self._growthRate):
      x = random.randint(0, self.x - 1)
      y = random.randint(0, self.y - 1)
      self._drops[x][y].append(self.z - 1)

    for x in range(self.x):
      for y in range(self.y):
        col = self._drops[x][y]
        if len(col) > 0:
          removals = []
          for z in range(len(col)):
            drop = col[z]
            if drop < self.z:
              self._drawDrop(x, y, drop)
            if drop + (self._tail - 1) >= 0:
              drop = drop - 1
              self._drops[x][y][z] = drop
            else:
              removals.append(drop)
          for r in removals:
            self._drops[x][y].remove(r)

    # TODO: Handle overflow
    self._step += amt