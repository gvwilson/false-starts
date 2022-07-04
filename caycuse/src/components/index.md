---
title: "Designing for Change"
---

-   [% g invasion_percolation "Invasion percolation" %] is a model of how a fluid percolates into a porous medium
    (or another fluid)
    -   Fill a grid with random numbers
    -   Mark the center cell as "filled"
    -   Repeatedly:
        -   Pick the lowest-valued cell adjacent to any filled cell
	-   Mark it as filled
    -   Until filling reaches the edge of the grid
-   Produces a fractal whose dimension depends on:
    -   The range of random values (i.e., how variable the porosity of the medium is)
    -   The connectivity of the grid (3-way, 4-way, 6-way, or 8-way)
-   We want to experiment with this, which means our code needs to:
    -   Represent several sizes of grids
    -   Represent several different kinds of connectivity
    -   Allow for different filling algorithms
-   Start by outlining the main program
    -   Parse command-line arguments
    -   Create and initialize grid
    -   Loop until filling hits edge

```{.python title="invperc.py"}
def main():
    """Parse arguments, run simulation, show result."""
    # Set up.
    options = parse_args()
    random.seed(options.seed)
    grid = World(options.x, options.y)
    initialize(grid, options)

    # Run until edge reached.
    while True:
        coords = find_next()
        grid[coords] = FILLED
        if grid.on_edge(coords):
            break
```

-   Start by implementing a 2D grid class (because we know how to do that)
    -   Store all values as 1D list rather than list of lists
    -   Want `grid[x, y]` rather than `grid.get(x, y)` or `grid.set(x, y, val)`
    -   So define `__getitem__` and `__setitem__`
    -   And the `on_edge` method the main program relied on

```{.python title="world.py"}
FILLED = -1  # Mark filled cells.

class World:
    """Store a rectangular 2D grid."""

    def __init__(self, x, y):
        """Construct an XY grid."""
        assert (0 < x) and (0 < y)
        self.dimX = x
        self.dimY = y
        self.cells = [0] * (self.dimX * self.dimY)

    def __getitem__(self, key):
        """Get a value from (x, y)."""
        self._checkIndex(key[0], key[1])
        return self.cells[key[0] * self.dimY + key[1]]

    def __setitem__(self, key, val):
        """Set a value at (x, y)."""
        self._checkIndex(key[0], key[1])
        self.cells[key[0] * self.dimY + key[1]] = val

    def on_edge(self, loc):
        """Is this point on the edge?"""
        ix, iy = loc
        return (ix == 0) or (ix == self.dimX - 1) or (iy == 0) or (iy == self.dimY - 1)

    def _checkIndex(self, ix, iy):
        """Check that an index is in range."""
        if (ix < 0) or (self.dimX < ix):
            raise IndexError("X index out of range")
        if (iy < 0) or (self.dimY < iy):
            raise IndexError("Y index out of range")
```

-   Connectivity is variable, so put it in a class of its own
    -   Define an [% g abstract_base_class "abstract base class" %] with shared code and placeholders
    -   Then derive concrete implementations
-   Abstract base class is:

```{.python title="connections.py"}
from abc import ABC, abstractmethod

from world import FILLED


class Connect:
    """Define connection operations."""
    def __init__(self, world):
        self.world = world

    def adjacent(self, loc):
        """Is this point adjacent to a filled cell?"""
        for pt in self.neighbors(loc):
            if self.world[pt] == FILLED:
                return True
        return False

    @abstractmethod
    def neighbors(self, loc):
        """Generate neighbor coordinates."""
```

-   Four-way connectivity uses a [% g generator "generator" %] to [% g yield "yield" %] neighbors
    -   So other code can use this method as the subject of a loop

```{.python title="connections.py"}
class Connect_4(Connect):
    """Four-way connectivity."""

    def neighbors(self, loc):
        """Generate neighbor coordinates."""
        ix, iy = loc
        dx, dy = self.world.dims()
        assert 0 <= ix < dx
        assert 0 <= iy < dy

        if 0 < ix:
            yield ix - 1, iy

        if ix < dx - 1:
            yield ix + 1, iy

        if 0 < iy:
            yield ix, iy - 1

        if iy < dy - 1:
            yield ix, iy + 1
```

-   Eight-way connectivity has the same interface but a different implementation

```{.python title="connections.py"}
class Connect_8(Connect):
    """Eight-way connectivity."""
    def neighbors(self, loc):
        """Eight-way connectivity."""
        ix, iy = loc
        dx, dy = self.world.dims()
        assert 0 <= ix < dx
        assert 0 <= iy < dy

        for x in (ix - 1, ix, ix + 1):
            if 0 <= x < dx:
                for y in (iy - 1, iy, iy + 1):
                    if 0 <= y < dy:
                        if (x != ix) or (y != iy):
                            yield x, y
```

-   Use a similar trick to create plug-and-play algorithms for finding and filling cells
-   Abstract base class for algorithm takes a grid and a connectivity object

```{.python title="algorithms.py"}
class Algorithm(ABC):
    """Base class for all algorithms."""

    def __init__(self, world, connect):
        """Construct shared values."""
        self.world = world
        self.connect = connect

    @abstractmethod
    def __call__(self):
        """Find the next cell to fill."""
```

-   Simplest algorithm sweeps the entire grid each time
    looking for the lowest-valued cell adjacent to a filled cell

```{.python title="algorithms.py"}
class Sweep(Algorithm):
    """Sweep the whole grid every time."""

    def __call__(self):
        """Find the next cell to fill."""
        dx, dy = self.world.dims()
        rx, ry, rv = None, None, None
        for ix in range(dx):
            for iy in range(dy):
                val = self.world[ix, iy]
                if (val != FILLED) and self.connect.adjacent((ix, iy)):
                    if (rv == None) or (val < rv):
                        rx, ry, rv = ix, iy, val
        if rv == None:
            raise ValueError("Cannot find cell to fill")
        return rx, ry
```

-   But wait: we might also want to change how we initialize the grid
    -   What if there's a spatial bias in the distribution of random values?
    -   Or barriers (i.e., non-porous regions)?
-   So put grid initialization in a class as well

```{.python title="initialize.py"}
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
```

-   Main program is now:

```{.python title="invperc.py"}
import algorithms, connections, initialize, render
from world import World, FILLED

ALGORITHMS = {
    "sweep": algorithms.Sweep,
    "window": algorithms.Window,
}

INITIALIZE = {
    "uniform": initialize.uniform
}

CONNECTIONS = {
    "4": connections.Connect_4,
    "8": connections.Connect_8
}


def main():
    """Parse arguments, run simulation, show result."""
    # Set up.
    options = parse_args()
    random.seed(options.seed)
    grid = World(options.x, options.y)
    INITIALIZE[options.init](grid, options)

    # Run until edge reached.
    connect = CONNECTIONS[options.connect](grid)
    alg = ALGORITHMS[options.algorithm](grid, connect)
    while True:
        coords = alg()
        grid[coords] = FILLED
        if grid.on_edge(coords):
            break
```

-   Specify initialization method, connectivity, and fill algorithm on command line
-   Each is a component with a fixed interface that only relies on the fixed interfaces of other components
-   Which makes plugging in a new component easy
-   For example, keep track of how wide and tall the filled region is and only search nearby
    -   Why bother searching cells that can't possibly be fillable?
-   Nothing else in the program has to change
-   And we don't have to implement this separately for each kind of connectivity

```{.python title="algorithms.py"}
class Window(Algorithm):
    """Only sweep the plausible region."""

    def __init__(self, world, connect):
        """Construct shared values."""
        self.world = world
        self.connect = connect

        cx, cy = self.world.center()
        self.loX = cx - 1
        self.loY = cy - 1
        self.hiX = cx + 1
        self.hiY = cy + 1

    def __call__(self):
        """Find the next cell to fill."""
        rx, ry, rv = None, None, None
        for ix in range(self.loX, self.hiX):
            for iy in range(self.loY, self.hiY):
                val = self.world[ix, iy]
                if (val != FILLED) and self.connect.adjacent((ix, iy)):
                    if (rv == None) or (val < rv):
                        rx, ry, rv = ix, iy, val

        if rv == None:
            raise ValueError("Cannot find cell to fill")

        self.loX = min(self.loX, rx - 1)
        self.loY = min(self.loY, ry - 1)
        self.hiX = max(self.hiX, rx + 1)
        self.hiY = max(self.hiY, ry + 1)

        return rx, ry
```

-   But what do these fractals look like?
-   Draw a picture (rather than a graph)

```{.python title="render.py"}
"""Render world grids."""

from PIL import Image, ImageDraw

from world import FILLED


BACKGROUND = (128, 128, 128)
FILL = (128, 128, 255)
SCALE = 10


def make_image(filename, grid):
    """Create and save an image of the fractal."""
    dx, dy = grid.dims()
    width = SCALE * dx
    height = SCALE * dy
    img = Image.new(mode="RGB", size=(width, height))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, SCALE * dx - 1, SCALE * dy - 1), fill=BACKGROUND, outline=FILL)
    for ix in range(dx):
        for iy in range(dx):
            if grid[(ix, iy)] != FILLED:
                continue
            draw.rectangle(
                (SCALE * ix, SCALE * iy, SCALE * (ix + 1) - 1, SCALE * (iy + 1) - 1),
                fill=FILL,
                outline=FILL
            )
    img.save(filename)
```

-   Run
-   Put key parameters in output filename

```bash
$ python invperc.py --seed 12345 --algorithm sweep --x 51 --y 51 --height 10 --image sweep-51x51-10-12345.png
```

[% figure
   slug="fractal-sweep-01"
   img="sweep-51x51-10-12345.png"
   caption="First Fractal"
   alt="Fractal produced by full sweep invasion percolation algorithm."
%]

-   That's kind of pretty
-   Let's try a different seed

```bash
$ python invperc.py --seed 67890 --algorithm sweep --x 51 --y 51 --height 10 --image sweep-51x51-10-67890.png
```

[% figure
   slug="fractal-sweep-01"
   img="sweep-51x51-10-67890.png"
   caption="Second Fractal"
   alt="Another fractal produced by full sweep invasion percolation algorithm."
%]

-   Should get exactly the same result using the windowed algorithm

```bash
$ python invperc.py --seed 12345 --algorithm window --x 51 --y 51 --height 10 --image window-51x51-10-12345.png
```

[% figure
   slug="fractal-window-01"
   img="window-51x51-10-12345.png"
   caption="Windowed Version of First Fractal"
   alt="Reproduction of first fractal using windowed algorithm."
%]

-   This isn't the same
-   Check that the grids are the same
    -   Yes: generating the same random numbers in the same sequence from the same seed

```{.python title="world.py"}
class World:
    """Store a rectangular 2D grid."""
    # ...as before...

    def __str__(self):
        """Convert to string for printing."""
        width = max(2, len(str(max(self.cells))))
        format = f"|%{width}s"
        ruler = "+" + ("-" * width)
        ruler = (ruler * self.dimX) + "+\n"
        result = ""
        iy = self.dimY - 1
        while iy >= 0:
            result += ruler
            for ix in range(self.dimX):
                val = self[ix, iy] if self[ix, iy] != FILLED else 'X'
                result += format % val
            result += "|\n"
            iy -= 1
        result += ruler
        return result
```

-   Run both algorithms on a 5x5 grid: very first cell filled is wrong for the windowing algorithm
-   Quickly spot that the windowed update `__call__` function was using:

```{.python title="algorithms.py"}
        for ix in range(self.loX, self.hiX + 1):
            for iy in range(self.loY, self.hiY + 1):
```

-   This skips the high edges
-   Should have been using:

```{.python title="algorithms.py"}
        for ix in range(self.loX, self.hiX + 1):
            for iy in range(self.loY, self.hiY + 1):
```

-   Re-run and yes, it produces the correct image
-   Which highlights one of the benefits of component-based software development: [% g cross_validation "cross-validation" %]
-   But now we're worried about whether there are other bugs
-   Run 100 times and count how often each cell in a 51x51 grid is filled

[% figure
   slug="merged-with-bug"
   img="merged-51x51-10-12345-300.png"
   caption="Merged Grids with Bug"
   alt="Heat map showing how often cells are filled with bug present."
%]

-   Appears to be bias
-   We are picking the lowest-valued cell on the boundary…
-   …and if there's a tie, the *first* one we see
-   So create another algorithm
    -   Derive from the fixed version of the window algorithm because we need the same initialization
    -   Save candidate cells, then choose one at random

```{.python title="algorithms.py"}
class WindowTies(WindowFixed):
    """Only sweep the plausible region."""
    def __call__(self):
        """Find the next cell to fill, choosing randomly between ties."""
        rv = None
        candidates = []
        for ix in range(self.loX, self.hiX + 1):
            for iy in range(self.loY, self.hiY + 1):
                rv = self._inspect(candidates, rv, ix, iy)

        if not candidates:
            raise ValueError("Cannot find cell to fill")

        rx, ry = random.choice(candidates)

        self.loX = min(self.loX, rx - 1)
        self.loY = min(self.loY, ry - 1)
        self.hiX = max(self.hiX, rx + 1)
        self.hiY = max(self.hiY, ry + 1)

        return rx, ry
```

-   Handle cases for a single cell
    -   Be careful to update `candidates` in place rather than assinging a completely new value
    -   I.e., `candidates = [(ix, iy)]` doesn't work

```{.python title="algorithms.py"}
    def _inspect(self, candidates, rv, ix, iy):
        """Handle inspection of a single cell."""
        val = self.world[ix, iy]
        if val == FILLED:
            pass

        elif not self.connect.adjacent((ix, iy)):
            pass

        elif (rv == None) or (val < rv):
            candidates.clear()
            candidates.append((ix, iy))
            rv = val

        elif val == rv:
            candidates.append((ix, iy))

        return rv
```

[% figure
   slug="merged-without-bug"
   img="ties-51x51-10-12345-300.png"
   caption="Merged Grids with Ties Handled Correctly"
   alt="Heat map showing how often cells are filled with ties handled."
%]
