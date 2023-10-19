import pygame
from constants import WIDTH, HEIGHT, FPS, SIDE
from board import Board
from character import Head, Body

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


def game():
    run = True
    clock = pygame.time.Clock()

    board = Board(win)
    board.create_board()

    character = [
        Head(win, SIDE * 2, SIDE * 0),
    ]
    character.append(Body(win, SIDE * 1, SIDE * 0, character[0]))
    character.append(Body(win, SIDE * 0, SIDE * 0, character[1]))

    for parts in character:
        parts.draw()

    pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        board.create_board()

        character[-2].make_body()
        character[-1].make_tail()

        for i in reversed(range(len(character))):
            character[i].move()
            character[i].draw()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    game()
