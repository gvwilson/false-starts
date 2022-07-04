"""Next-fill algorithms."""

from abc import ABC, abstractmethod
import bisect
import random

from world import FILLED


class Algorithm(ABC):
    """Base class for all algorithms."""

    def __init__(self, world, connect):
        """Construct shared values."""
        self.world = world
        self.connect = connect

    @abstractmethod
    def __call__(self):
        """Find the next cell to fill."""


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


class WindowFixed(Algorithm):
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
        for ix in range(self.loX, self.hiX + 1):
            for iy in range(self.loY, self.hiY + 1):
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
