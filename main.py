import pygame as pg
import random
from settings import *

# Initial Setup
pg.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("2048")
timer = pg.time.Clock()
font = pg.font.Font("freesansbold.ttf", 24)


# Color Library
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          "light text": (249, 246, 242),
          "dark text": (119, 110, 101),
          "other": (0, 0, 0),
          "bg": (187, 173, 160)}


# Draw Board Background
def draw_board():
    pg.draw.rect(screen, (200, 200, 200), [0, 0, 400, 400], 0, 10)
    pass


# Draw Game Tiles
def draw_pieces():
    pass


# Main Game Loop
run = True
while run:
    timer.tick(FPS)
    screen.fill("gray")
    draw_board()
    draw_pieces()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
