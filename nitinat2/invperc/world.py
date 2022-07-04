"""The 2D world used for invasion percolation simulation.
$Id: world.py 2 2002-12-19 22:30:20Z gvwilson $
"""

class World:

  def __init__(self, x, y):
    assert (0 < x) and (0 < y)
    self.dimX = x
    self.dimY = y
    self.cells = [0] * (self.dimX * self.dimY)

  def __len__(self):
    return self.dimX * self.dimY

  def dimX(self):
    return self.dimX

  def dimY(self):
    return self.dimY

  def dims(self):
    return self.dimX, self.dimY

  def center(self):
    return self.dimX/2, self.dimY/2

  def __getitem__(self, key):
    self.checkIndex(key[0], key[1])
    return self.cells[key[0] * self.dimY + key[1]]

  def __setitem__(self, key, val):
    self.checkIndex(key[0], key[1])
    self.cells[key[0] * self.dimY + key[1]] = val

  def randomize(self, rand):
    for i in range(len(self.cells)):
      self.cells[i] = rand()

  def __str__(self):
    maxPos = len("%d" % max(self.cells))
    maxNeg = len("%d" % min(self.cells))
    width = max(maxPos, maxNeg)
    format = "|%" + `width` + "d"
    ruler = "+" + ("-" * width)
    ruler = (ruler * self.dimX) + "+\n"
    result = ""
    iy = self.dimY - 1
    while iy >= 0:
      result += ruler
      for ix in range(self.dimX):
        result += format % self[ix, iy]
      result += "|\n"
      iy -= 1
    result += ruler
    return result

  def checkIndex(self, ix, iy):
    if (ix < 0) or (self.dimX < ix):
      raise IndexError, "X index out of range"
    if (iy < 0) or (self.dimY < iy):
      raise IndexError, "Y index out of range"

if __name__ == "__main__":
  import sys, string
  dimX = string.atoi(sys.argv[1])
  dimY = string.atoi(sys.argv[2])
  world = World(dimX, dimY)
  val = 1
  print world
  for ix in range(dimX):
    for iy in range(dimY):
      world[ix, iy] = val
      val += 1
      print world
  world[world.center()] = -1
  print world
