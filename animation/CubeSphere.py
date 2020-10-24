from bibliopixel.animation.cube import Cube
import math


def genCubeVector(x, y, z, x_mult=1, y_mult=1, z_mult=1):
    """Generates a map of vector lengths from the center point to each coordinate
    x - width of matrix to generate
    y - height of matrix to generate
    z - depth of matrix to generate
    x_mult - value to scale x-axis by
    y_mult - value to scale y-axis by
    z_mult - value to scale z-axis by
    """
    cX = (x - 1) / 2.0
    cY = (y - 1) / 2.0
    cZ = (z - 1) / 2.0

    def vect(_x, _y, _z):
        return int(math.sqrt(math.pow(_x - cX, 2 * x_mult) +
                             math.pow(_y - cY, 2 * y_mult) +
                             math.pow(_z - cZ, 2 * z_mult)))

    return [[[vect(_x, _y, _z) for _z in range(z)] for _y in range(y)] for _x in range(x)]


class CubeSphere(Cube):

    def __init__(self, layout, dir=True, **kwds):
        super().__init__(layout, **kwds)
        self._vector = genCubeVector(self.x, self.y, self.z)
        self._dir = dir

    def pre_run(self):
        self._step = 0

    def step(self, amt=1):
        self.layout.all_off()
        traveling_up = (self._step // self.z) % 2 == 0
        radius = (self._step % self.z) if traveling_up else (self.z - (self._step % self.z))

        # this respects master brightness but is slower
        for z in range(self.z):
            for y in range(self.y):
                for x in range(self.x):
                    if self._vector[x][y][z] == radius:
                        self.layout.set(x, y, z, (255,255,255))

        # TODO: Handle overflow
        self._step += 1