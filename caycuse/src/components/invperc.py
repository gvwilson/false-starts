"""Main driver for invasion percolation."""

import argparse
import random
import sys
import algorithms, connections, initialize, render
from world import World, FILLED


ALGORITHMS = {
    "sweep": algorithms.Sweep,
    "window": algorithms.WindowFixed,
    "ties": algorithms.WindowTies
}

INITIALIZE = {"uniform": initialize.uniform}

CONNECTIONS = {"4": connections.Connect_4, "8": connections.Connect_8}

SETTINGS = {
    "algorithm": "sweep",
    "connections": "4",
    "init": "uniform",
    "height": 2,
    "dimX": 5,
    "dimY": 5,
    "seed": None,
    "number": 1,
}


def main():
    """Parse arguments, run simulation, show result."""
    # Set up.
    options = parse_args()
    random.seed(options.seed)
    merged = World(options.x, options.y)
    for i in range(options.number):
        grid = grow(options)
        combine(merged, grid)

    if options.image is not None:
        render.make_image(options.image, merged, options.number)


def combine(accum, grid):
    """Combine fractal into running total."""
    assert accum.dims() == grid.dims()
    dx, dy = accum.dims()
    for ix in range(dx):
        for iy in range(dy):
            increment = 1 if grid[ix, iy] == FILLED else 0
            accum[ix, iy] = accum[ix, iy] + increment


def grow(options):
    """Grow a single grid."""
    grid = World(options.x, options.y)
    INITIALIZE[options.init](grid, options)

    connect = CONNECTIONS[options.connect](grid)
    alg = ALGORITHMS[options.algorithm](grid, connect)
    loop = -1
    while True:
        loop += 1
        if options.trace:
            render.show(f"loop {loop}", grid)
        coords = alg()
        grid[coords] = FILLED
        if grid.on_edge(coords):
            break

    if options.trace:
        render.show("final", grid)

    return grid


def parse_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--algorithm",
        choices=ALGORITHMS.keys(),
        default=SETTINGS["algorithm"],
        help="update algorithm",
    )
    parser.add_argument(
        "--connect",
        choices=CONNECTIONS.keys(),
        default=SETTINGS["connections"],
        help="grid connectivity",
    )
    parser.add_argument(
        "--init",
        choices=INITIALIZE.keys(),
        default=SETTINGS["init"],
        help="initialization method",
    )
    parser.add_argument(
        "--height", type=int, default=SETTINGS["height"], help="range of random values"
    )
    parser.add_argument("--x", type=int, default=SETTINGS["dimX"], help="grid X size")
    parser.add_argument("--y", type=int, default=SETTINGS["dimY"], help="grid Y size")
    parser.add_argument("--seed", type=int, default=SETTINGS["seed"], help="random number seed")
    parser.add_argument("--trace", action="store_true", default=False, help="trace execution")
    parser.add_argument("--image", default=None, help="save result as image file")
    parser.add_argument("--number", type=int, default=SETTINGS["number"], help="number to run and merge")
    return parser.parse_args()


if __name__ == "__main__":
    main()
