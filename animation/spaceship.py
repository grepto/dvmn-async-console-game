import asyncio
import os

from animation.curses_tools import draw_frame, get_frame_size, read_controls

FRAME_DIR = os.path.join('animation', 'frames')


async def spaceship(canvas, start_row, start_column):
    with open(os.path.join(FRAME_DIR, 'rocket_frame_1.txt'), 'r') as rocket:
        frame1 = rocket.read()
    with open(os.path.join(FRAME_DIR, 'rocket_frame_2.txt'), 'r') as rocket:
        frame2 = rocket.read()

    canvas_height, canvas_width = canvas.getmaxyx()
    frame_height, frame_width = get_frame_size(frame1)
    border_width = 1

    row, column = start_row + 1, start_column - round(frame_width / 2)

    motion_space_width = canvas_width - frame_width - border_width
    motion_space_height = canvas_height - frame_height - border_width

    while True:
        draw_frame(canvas, row, column, frame2, negative=True)
        rows_direction, columns_direction, space_pressed = read_controls(canvas)

        if rows_direction:
            row = min(row + rows_direction, motion_space_height) if rows_direction > 0 else max(row + rows_direction, 1)

        if columns_direction:
            column = min(column + columns_direction, motion_space_width) if columns_direction > 0 else max(column + columns_direction, 1)

        draw_frame(canvas, row, column, frame1)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, frame1, negative=True)
        draw_frame(canvas, row, column, frame2)
        await asyncio.sleep(0)
