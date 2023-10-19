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
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(
            self.win,
            RED,
            (self.x + (SIDE // 2), self.y + (SIDE // 2)),
            (SIDE // 2) - 10,
        )
