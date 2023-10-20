import pygame
from constants import ROWS, COLS, SIDE, GREEN, MINT, RED


class Board:
    def __init__(self, win):
        self.win = win

    def create_board(self):
        self.win.fill(GREEN)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(self.win, MINT, (row * SIDE, col * SIDE, SIDE, SIDE))


class Apple:
    def __init__(self, win):
        self.win = win
        self.x = None
        self.y = None

    def draw(self):
        pygame.draw.circle(
            self.win,
            RED,
            (self.x + (SIDE // 2), self.y + (SIDE // 2)),
            (SIDE // 2) - 10,
        )

    def set_position(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
