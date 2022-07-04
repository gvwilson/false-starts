"""Randomizers for invasion percolation simulation.
$Id: initialize.py 2 2002-12-19 22:30:20Z gvwilson $
"""

from random import Random

class Uniform:

  def __init__(self, ceiling, seed=None):
    assert 0 < ceiling
    self.g = Random(seed)
    self.ceiling = ceiling

  def __call__(self):
    return self.g.randrange(self.ceiling)

if __name__ == "__main__":

  import sys, string, getopt
  choices, remainder = getopt.getopt(sys.argv[1:], "bn:s:u:")
  if remainder:
    print >> sys.stderr, "Trailing arguments", remainder
    sys.exit(1)
  number = 1
  ceiling = None
  seed = None
  for (flag, val) in choices:
    if flag == "-n":
      number = string.atoi(val)
    elif flag == "-s":
      seed = string.atoi(val)
    elif flag == "-u":
      ceiling = string.atoi(val)
    else:
      print >> sys.stderr, "Unknown flag '%s'" % flag
      sys.exit(1)

  r = Uniform(ceiling, seed)
  values = {}
  for i in range(number):
    v = r()
    values[v] = values.get(v, 0) + 1

  keys = values.keys()
  keys.sort()
  for k in keys:
    print "%4d\t%4d" % (k, values[k])
