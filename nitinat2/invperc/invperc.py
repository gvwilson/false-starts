"""Main driver module for invasion percolation.
$Id: invperc.py 2 2002-12-19 22:30:20Z gvwilson $
"""

import sys, getopt
import connections, initialize, algorithms
from world import World

def parseArgs(args):

  algDict = {
    "sweep"  : algorithms.Sweep,
    "window" : algorithms.Window,
    "prique" : algorithms.Prique
  }

  connectDict = {
    "4" : connections.connect_4,
    "8" : connections.connect_8
  }

  settings = {
    "algorithm"    : algorithms.Prique,
    "range"        : 2,
    "connectivity" : connections.connect_4,
    "fraction"     : 0.50,
    "dimX"         : 5,
    "dimY"         : 5,
    "traceFile"    : None,
    "worldfile"    : None
  }

  help = """invperc: invasion percolation simulator
  -a   algorithm     (sweep, window, prique)
  -c   connectivity  (4, 8)
  -f   fraction      (0.0 ... 1.0)
  -h   help
  -r   range         (positive integer)
  -t   tracefile
  -w   worldfile
  -x   X dimension   (positive integer)
  -y   Y dimension   (positive integer)"""

  choices, remainder = getopt.getopt(args, "a:c:f:hr:t:w:x:y:")
  if remainder:
    print >> sys.stderr, "Trailing arguments", remainder
    sys.exit(1)

  for (flag, arg) in choices:

    # Algorithm choice
    if flag == "-a":
      try:
        algorithm = algDict[arg]
      except KeyError:
        print >> sys.stderr, "Unknown algorithm '%s'" % arg
        sys.exit(1)

    # Connectivity
    elif flag == "-c":
      try:
        connectivity = connectDict[arg]
      except KeyError:
        print >> sys.stderr, "Unknown connectivity '%s'" % arg
        sys.exit(1)

    # Fraction to fill
    elif flag == "-f":
      try:
        fraction = string.atof(arg)
        if (fraction < 0.0) or (1.0 < fraction):
          raise ValueError
      except ValueError:
        print >> sys.stderr, "Bad fraction '%s'" % arg
        sys.exit(1)

    # Help
    elif flag == "-h":
      help()
      sys.exit(0)

    # Range of values
    elif flag == "-r":
      try:
        initialize = string.atoi(arg)
        if initialize < 2:
          raise ValueError
      except ValueError:
        print >> sys.stderr, "Bad initialization range '%s'" % arg
        sys.exit(1)

    # Trace steps in filling
    elif flag == "-t":
      traceFile = arg

    # Store final world
    elif flag == "-w":
      worldFile = arg

    # X dimension
    elif flag == "-x":
      try:
        dimX = string.atoi(arg)
        if dimX <= 0:
          raise ValueError
      except ValueError:
        print >> sys.stderr, "Bad X dimension '%s'" % arg
        sys.exit(1)

    # Y dimension
    elif flag == "-y":
      try:
        dimY = string.atoi(arg)
        if dimY <= 0:
          raise ValueError
      except ValueError:
        print >> sys.stderr, "Bad Y dimension '%s'" % arg
        sys.exit(1)

    # Unknown
    else:
      print >> sys.stderr, "Unknown flag '%s'" % flag
      sys.exit(1)

  return settings

if __name__ == "__main__":

  settings = parseArgs(sys.argv[1:])
  print settings
