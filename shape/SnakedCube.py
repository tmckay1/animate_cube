from bibliopixel.util import log
from bibliopixel.colors import conversions
from bibliopixel.layout import font
from bibliopixel.layout.cube import Cube
from bibliopixel.layout.geometry.rotation import rotate_and_flip
from bibliopixel.layout.geometry.cube import make_cube_coord_map_positions
from bibliopixel.layout.geometry.matrix import make_matrix_coord_map
import math, threading, time


def make_cube_coord_map(dx, dy, dz, xy_serpentine=True, offset=0,
                        xy_rotation=0, z_rotation=0, z_flip=False):
    result = []
    plane_offset = offset
    for z in range(dz):
        odd = z % 2 == 1
        plane = make_matrix_coord_map(dx, dy, serpentine=xy_serpentine,
                                      offset=plane_offset, rotation=0,
                                      y_flip=(True if odd else False))
        plane_offset += (dx * dy)
        result.append(plane)

    result = rotate_and_flip(result, z_rotation, z_flip)

    return result

class SnakedCube(Cube):
    def __init__(self, drivers, x, y, z, coord_map=None,
                 threadedUpdate=False, brightness=255, **kwargs):
        super().__init__(drivers, x, y, z, coord_map=coord_map,
                 threadedUpdate=threadedUpdate, brightness=brightness, **kwargs)
        self.coord_map = make_cube_coord_map(x, y, z)
        self.set_pixel_positions(make_cube_coord_map_positions(self.coord_map))