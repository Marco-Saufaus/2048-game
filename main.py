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


# Initialize Game variables
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = ""


# Take Turn based on Direction
def take_turn(direction, board):
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direction == "UP":
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        board[i - shift][j] = board[i][j]
                        board[i][j] = 0
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift - 1][j] \
                            and not merged[i - shift][j]:
                        board[i - shift - 1][j] *= 2
                        board[i - shift][j] = 0
                        merged[i - shift - 1][j] = True
    elif direction == "DOWN":
        for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board[3 - q][j] == 0:
                        shift += 1
                if shift > 0:
                    board[2 - i + shift][j] = board[2 - i][j]
                    board[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board[2 - i + shift][j] == board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                            and not merged[2 - i + shift][j]:
                        board[3 - i + shift][j] *= 2
                        board[2 - i + shift][j] = 0
                        merged[3 - i + shift][j] = True
    elif direction == "LEFT":
        pass
    elif direction == "RIGHT":
        pass

    return board


# Spawn New
def new_pieces(board):
    count = 0
    full = False
    while any(0 in row for row in board) and count < 1:
        row = random.randint(0, 3)
        column = random.randint(0, 3)
        if board[row][column] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                board[row][column] = 4
            else:
                board[row][column] = 2
    if count < 1:
        full = True
    return board, full


# Draw Board Background
def draw_board():
    pg.draw.rect(screen, colors["bg"], [0, 0, 400, 400], 0, 10)
    pass


# Draw Game Tiles
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors["light text"]
            else:
                value_color = colors["dark text"]
            if value <= 2048:
                color = colors[value]
            else:
                color = colors["other"]
            pg.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 10)
            if value > 0:
                value_len = len(str(value))
                font = pg.font.Font("freesansbold.ttf", 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pg.draw.rect(screen, "black", [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)


# Main Game Loop
run = True
while run:
    timer.tick(FPS)
    screen.fill("gray")
    draw_board()
    draw_pieces(board_values)
    if spawn_new or init_count < 2:
        board_values, game_over = new_pieces(board_values)
        spawn_new = False
        init_count += 1
    if direction != "":
        board_values = take_turn(direction, board_values)
        direction = ""
        spawn_new = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                direction = "UP"
            elif event.key == pg.K_DOWN:
                direction = "DOWN"
            elif event.key == pg.K_LEFT:
                direction = "LEFT"
            elif event.key == pg.K_RIGHT:
                direction = "RIGHT"

    pg.display.flip()
