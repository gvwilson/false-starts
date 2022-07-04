"""2D grid for invasion percolation simulation."""

FILLED = -1  # Mark filled cells.


class World:
    """Store a rectangular 2D grid."""

    def __init__(self, x, y):
        """Construct an XY grid."""
        assert (0 < x) and (0 < y)
        self.dimX = x
        self.dimY = y
        self.cells = [0] * (self.dimX * self.dimY)

    def __len__(self):
        """Number of cells."""
        return self.dimX * self.dimY

    def dimX(self):
        """Size on X axis."""
        return self.dimX

    def dimY(self):
        """Size on Y axis."""
        return self.dimY

    def dims(self):
        """Both sizes."""
        return self.dimX, self.dimY

    def center(self):
        """Coordinates of grid center."""
        return self.dimX // 2, self.dimY // 2

    def on_edge(self, loc):
        """Is this point on the edge?"""
        ix, iy = loc
        return (ix == 0) or (ix == self.dimX - 1) or (iy == 0) or (iy == self.dimY - 1)

    def __getitem__(self, key):
        """Get a value from (x, y)."""
        self._checkIndex(key[0], key[1])
        return self.cells[key[0] * self.dimY + key[1]]

    def __setitem__(self, key, val):
        """Set a value at (x, y)."""
        self._checkIndex(key[0], key[1])
        self.cells[key[0] * self.dimY + key[1]] = val

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

    def _checkIndex(self, ix, iy):
        """Check that an index is in range."""
        if (ix < 0) or (self.dimX < ix):
            raise IndexError("X index out of range")
        if (iy < 0) or (self.dimY < iy):
            raise IndexError("Y index out of range")
