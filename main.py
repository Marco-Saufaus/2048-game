import pygame as pg
import random
from settings import *

# Initial Setup
pg.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("2048")
timer = pg.time.Clock()
font = pg.font.Font("freesansbold.ttf", 24)

# Main Game Loop
run = True
while run:
    timer.tick(FPS)
    screen.fill("gray")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
