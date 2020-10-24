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


class Firework(Cube):

    def __init__(self, layout, speed=1, **kwds):
        super().__init__(layout, **kwds)
        self._vector = genCubeVector(self.x, self.y, self.z)
        self._dir = dir
        self._speed = speed
        self._start_x = (self.x - 1) / 2
        self._start_y = (self.y - 1) / 2

    def pre_run(self):
        self._step = 0

    def step(self, amt=1):
        if (self._step % self._speed) == 0:
            self.layout.all_off()
            new_step = (self._step // self._speed)

            # draw a line for the first third of the animation, then the circle for the rest
            full_cycle_length = (3 * self.z / 2)
            cycle_step = new_step % cycle_length
            line_cycle_length = (self.z / 2)
            draw_circle = cycle_step >= line_cycle_length

            if draw_circle:
                # this respects master brightness but is slower
                radius = (new_step - line_cycle_length) % self.z
                for z in range(self.z):
                    for y in range(self.y):
                        for x in range(self.x):
                            if self._vector[x][y][z] == radius:
                                self.layout.set(x, y, z, self.palette((new_step * 2 // 3) % 255))
            else:
                self.layout.set(self._start_x, self._start_y, cycle_step, (255,165,0))

        # TODO: Handle overflow
        self._step += 1