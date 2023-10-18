import pygame
from constants import ROWS, COLS, SIDE, GREEN, MINT


class Board:
    def __init__(self, win):
        self.win = win

    def create_board(self):
        self.win.fill(GREEN)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(self.win, MINT, (row * SIDE, col * SIDE, SIDE, SIDE))
