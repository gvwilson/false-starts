"""Initialize invasion percolation simulation."""

import random

from world import FILLED


def uniform(world, options):
    """Initialize grid with uniform random numbers."""
    dimX, dimY = world.dims()
    for ix in range(dimX):
        for iy in range(dimY):
            world[ix, iy] = random.randrange(options.height)
    world[world.center()] = FILLED
