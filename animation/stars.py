import asyncio
import curses
import random


async def blink(canvas, row, column, offset_tics, symbol='*'):
    while True:

        for i in range(offset_tics):
            canvas.addstr(row, column, symbol, curses.A_DIM)
            await asyncio.sleep(0)

        for i in range(3):
            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)

        for i in range(5):
            canvas.addstr(row, column, symbol, curses.A_BOLD)
            await asyncio.sleep(0)

        for i in range(3):
            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)


def get_stars(canvas, symbols='+*.:', quantity=50):
    height, width = canvas.getmaxyx()

    coroutines = []
    for i in range(quantity):
        row = random.randint(1, height - 2)
        column = random.randint(1, width - 2)
        symbol = random.choice(symbols)
        offset_tics = random.randint(5, 20)
        coroutine = blink(canvas, row, column, offset_tics, symbol)
        coroutines.append(coroutine)

    return coroutines
