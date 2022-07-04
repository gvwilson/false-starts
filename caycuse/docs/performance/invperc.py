"""Main driver for invasion percolation."""

import argparse
import sys
import algorithms, connections, initialize, render
from world import World, FILLED


ALGORITHMS = {
    "sweep": algorithms.Sweep,
    "window": algorithms.Window,
    "prique": algorithms.Prique
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
}


def main():
    """Parse arguments, run simulation, show result."""
    # Set up.
    options = parse_args()
    grid = World(options.x, options.y)
    INITIALIZE[options.init](grid, options)

    # Run until edge reached.
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

    # Display.
    if options.trace:
        render.show("final", grid)
    if options.image is not None:
        render.make_image(options.image, grid)


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
    return parser.parse_args()


if __name__ == "__main__":
    main()
