import pygame
from constants import WIDTH, HEIGHT, FPS
from board import Board
from character import Head

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


def game():
    run = True
    clock = pygame.time.Clock()

    board = Board(win)
    board.create_board()

    character = Head(win, 0, 0)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        character.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    game()
