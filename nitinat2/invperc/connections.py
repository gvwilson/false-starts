"""Cell connection rules for invasion percolation.
$Id: connections.py 2 2002-12-19 22:30:20Z gvwilson $
"""

def connect_4(world, ix, iy):
  dx, dy = world.dims()
  assert 0 <= ix < dx
  assert 0 <= iy < dy
  result = []
  if 0 < ix:
    result.append((world[ix-1, iy]), ix-1, iy)
  if ix < dx-1:
    result.append((world[ix+1, iy]), ix+1, iy)
  if 0 < iy:
    result.append((world[ix, iy-1], ix, iy-1))
  if iy < dy-1:
    result.append((world[ix, iy+1], ix, iy+1))
  return result

def connect_8(world, ix, iy):
  dx, dy = world.dims()
  assert 0 <= ix < dx
  assert 0 <= iy < dy
  result = []
  for x in (ix-1, ix, ix+1):
    if 0 <= x < dx:
      for y in (iy-1, iy, iy+1):
        if 0 <= y < dy:
          if (x != ix) or (y != iy):
            result.append((world[x, y], x, y))
  return result

