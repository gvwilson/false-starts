"""Next-fill algorithm that sweeps the entire grid.
$Id: algorithms.py 2 2002-12-19 22:30:20Z gvwilson $
"""

import bisect

class Algorithm:

  def __init__(self, world, filled, connect):
    self.world = world
    self.filled = filled
    self.connect = connect

  def adjacent(self, ix, iy):
    return False

class Sweep(Algorithm):

  def __init__(self, world, filled, connect):
    Algorithm.__init__(self, world, filled, connect)

  def __call__(self):
    dx, dy = self.world.dims()
    rx, ry, rv = None, None, None
    for ix in range(dx):
      for iy in range(dy):
        val = world[ix, iy]
        if (val != self.filled) and self.adjacent(ix, iy):
          if (rv == None) or (val < rv):
            rx, ry, rv = ix, iy, val
    if rv == None:
      raise ValueError, "Whole world filled"
    return rx, ry

class Window(Algorithm):

  def __init__(self, world, filled, connect):
    Algorithm.__init__(self, world, filled, connect)
    self.loX = 0
    self.loY = 0
    self.hiX = world.dimX()
    self.hiY = world.dimY()

  def __call__(self):
    rx, ry, rv = None, None, None
    for ix in range(self.loX, self.hiX):
      for iy in range(self.loY, self.hiY):
        val = world[ix, iy]
        if (val != self.filled) and self.adjacent(ix, iy):
          if (rv == None) or (val < rv):
            rx, ry, rv = ix, iy, val
    if rv == None:
      raise ValueError, "Whole world filled"
    self.loX = min(self.loX, rx)
    self.loY = min(self.loY, ry)
    self.hiX = max(self.hiX, rx+1)
    self.hiY = max(self.hiY, ry+1)
    return rx, ry

class Prique(Algorithm):

  def __init__(self, world, filled, connect):
    Algorithm.__init__(self, world, filled, connect)
    self.queue = []

  def __call__(self):

    if not self.queue:
      center = cx, cy
      self.queue = [(world[cx, cy], cx, cy)]

    choice, self.queue = self.queue[0], self.queue[1:]
    cv, cx, cy = choice
    neighbors = self.connect.neighbors(world, ix, iy)
    for nv, nx, ny in neighbors:
      if (nv != self.filled):
        bisect.insort(self.queue, (nv, nx, ny))

    return cx, cy
