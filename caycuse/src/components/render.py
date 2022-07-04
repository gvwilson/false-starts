"""Render world grids."""

from PIL import Image, ImageDraw

from world import FILLED


BACKGROUND = (255, 255, 255)
FILL = (64, 64, 128)
SCALE = 10


def make_image(filename, grid, number):
    """Create and save an image of the fractal."""
    dx, dy = grid.dims()
    width = SCALE * dx
    height = SCALE * dy
    img = Image.new(mode="RGB", size=(width, height))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, SCALE * dx - 1, SCALE * dy - 1), fill=BACKGROUND, outline=FILL)
    for ix in range(dx):
        for iy in range(dx):
            if number == 1:
                draw_fractal(draw, grid, ix, iy)
            else:
                draw_scaled(draw, grid, ix, iy, number)
    img.save(filename)


def draw_fractal(draw, grid, ix, iy):
    if grid[ix, iy] != FILLED:
        return
    draw.rectangle(
        (SCALE * ix, SCALE * iy, SCALE * (ix + 1) - 1, SCALE * (iy + 1) - 1),
        fill=FILL,
        outline=FILL
    )


def draw_scaled(draw, grid, ix, iy, divisor):
    color = int(256 * grid[ix, iy] / divisor)
    color = (color, color, color)
    draw.rectangle(
        (SCALE * ix, SCALE * iy, SCALE * (ix + 1) - 1, SCALE * (iy + 1) - 1),
        fill=color,
        outline=color
    )


def show(title, grid):
    """Show grid for debugging."""
    print(title)
    print(grid)
