import pygame as pg
import random
from settings import *


pg.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("2048")
timer = pg.time.Clock()
font = pg.font.Font("freesansbold.ttf", 24)

