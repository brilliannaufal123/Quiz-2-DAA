import pygame

WIN_W = 1500
WIN_H = 950
FPS = 60
BASE_COL = 9
BASE_ROWS = 7
CELLS_ADDED = 2
SCREEN_MARGIN = 10
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def oddnum(n):
    if n % 2 == 0:
        n = n - 1
    return n

def get_level_dims(level):#get level dimensions based on level number
    raw_col = BASE_COL + (level - 1) * CELLS_ADDED
    raw_rows = BASE_ROWS + (level - 1) * CELLS_ADDED

    col = oddnum(raw_col)
    rows = oddnum(raw_rows)

    available_width = WIN_W - (SCREEN_MARGIN * 2)
    available_height = WIN_H - (SCREEN_MARGIN * 2)

    cell_w = int(available_width / col)
    cell_h = int(available_height / rows)

    cell_size = min(cell_w, cell_h)

    return col, rows, cell_size
#set colors
COLORS = {
    "background":(30, 30, 30),
    "grid_lines":(0, 0, 0),
    "player": (0,0,255),
    "trail":(160, 174,230),
    "end_point":(255,0,0),
    "dfs_path":(235,142, 45),
    "ui_card":(250, 248,242),
    "text_main":(125,125,125),
    "green_color":(63,173,118),
    "red_color":(220,87, 87),
}