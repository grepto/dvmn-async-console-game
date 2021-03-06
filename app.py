import curses
import time

from animation.shot import fire
from animation.spaceship import spaceship
from animation.stars import get_stars

TIC_TIMEOUT = 0.1


def draw(canvas):
    canvas.border()
    canvas.nodelay(True)
    curses.curs_set(False)

    height, width = canvas.getmaxyx()
    center_row = round(height / 2)
    center_column = round(width / 2)

    stars = get_stars(canvas, quantity=200)
    shot = fire(canvas, center_row, center_column)
    rocket = spaceship(canvas, center_row, center_column)

    coroutines = [
        *stars,
        shot,
        rocket
    ]

    while coroutines:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)

        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
