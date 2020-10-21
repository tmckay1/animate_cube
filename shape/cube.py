from bibliopixel.util import log
from bibliopixel.colors import conversions
from bibliopixel.layout import font
from bibliopixel.layout.layout import Layout
# from bibliopixel.layout.geometry.cube import make_cube_coord_map, make_cube_coord_map_positions
from bibliopixel.layout.geometry.rotation import rotate_and_flip
from bibliopixel.layout.geometry.matrix import make_matrix_coord_map
import math, threading, time


def make_cube_coord_map(dx, dy, dz, xy_serpentine=True, offset=0,
                        xy_rotation=0, z_rotation=0,
                        y_flip=False, z_flip=False):
    result = []
    plane_offset = offset
    for z in range(dz):
        plane = make_matrix_coord_map(dx, dy, serpentine=xy_serpentine,
                                      offset=plane_offset, rotation=xy_rotation,
                                      y_flip=y_flip)
        plane_offset += (dx * dy)
        result.append(plane)

    result = rotate_and_flip(result, z_rotation, z_flip)

    return result


def make_cube_coord_map_positions(coord_map):
    num = 0
    dx, dy, dz = (0, 0, len(coord_map))

    for xy in coord_map:
        if len(xy) > dx:
            dy = len(xy)
        for x in xy:
            if len(x) > dx:
                dx = len(x)
            num += len(x)

    result = [None] * num
    for z in range(dz):
        for y in range(dy):
            for x in range(dx):
                result[coord_map[z][y][x]] = [x, y, z]
    return result

class Cube(Layout):
    CLONE_ATTRS = Layout.CLONE_ATTRS + ('x', 'y', 'z')

    def __init__(self, drivers, x, y, z, coord_map=None,
                 threadedUpdate=False, brightness=255, **kwargs):
        super().__init__(drivers, threadedUpdate, brightness, **kwargs)
        self.x = x
        self.y = y
        self.z = z

        if self.x * self.y * self.z != self.numLEDs:
            raise TypeError("(x * y * z) MUST equal the total pixel count!")

        if coord_map:
            self.coord_map = coord_map
        else:
            if len(self.drivers) == 1:
                self.coord_map = make_cube_coord_map(x, y, z)
            else:
                raise TypeError(
                    "Must provide coord_map if using multiple drivers!")

        self.set_pixel_positions(make_cube_coord_map_positions(self.coord_map))

    def get_pixel_positions(self):
        return make_cube_coord_map_positions(self.coord_map)

    @property
    def shape(self):
        """Returns ``x, y, z``"""
        return self.x, self.y, self.z

    def set(self, x, y, z, color):
        try:
            pixel = self.coord_map[z][y][x]
            self._set_base(pixel, color)
        except IndexError:
            pass

    def get(self, x, y, z):
        try:
            pixel = self.coord_map[z][y][x]
            return self._get_base(pixel)
        except IndexError:
            return 0, 0, 0

    def setHSV(self, x, y, z, hsv):
        color = conversions.hsv2rgb(hsv)
        self._set(x, y, z, color)

    def setRGB(self, x, y, z, r, g, b):
        color = (r, g, b)
        self._set(x, y, z, color)