"""Cell connection rules for invasion percolation."""

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
