import pygame
from constants import WIDTH, HEIGHT, FPS, SIDE, FONT
from board import Board
from character import Head, Body

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


def check_collsion(character):
    # Check if head goes beyond the boundaries.
    if character[0].get_x() < 0 or character[0].get_x() >= WIDTH:
        return True
    elif character[0].get_y() < 0 or character[0].get_y() >= HEIGHT:
        return True

    # Check for head collsion with body or tail.
    for i in range(1, len(character)):
        if (
            character[0].get_x() == character[i].get_x()
            and character[0].get_y() == character[i].get_y()
        ):
            return True

    return False


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
    character.append(Body(win, SIDE * 0, SIDE * 0, character[2]))
    character.append(Body(win, SIDE * 0, SIDE * 0, character[3]))
    character.append(Body(win, SIDE * 0, SIDE * 0, character[4]))
    character.append(Body(win, SIDE * 0, SIDE * 0, character[5]))
    character.append(Body(win, SIDE * 0, SIDE * 0, character[6]))
    character.append(Body(win, SIDE * 0, SIDE * 0, character[7]))

    # for parts in character:
    #     parts.draw()

    # pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if check_collsion(character):
            print("collided")
            game_over_text = FONT.render("Game Over...", 1, "white")
            win.blit(
                game_over_text,
                (
                    WIDTH // 2 - game_over_text.get_width() // 2,
                    HEIGHT // 2 - game_over_text.get_height() // 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(5000)
            run = False
            break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not character[0].get_orientation() == "right":
            character[0].set_orientation("left")
        elif keys[pygame.K_RIGHT] and not character[0].get_orientation() == "left":
            character[0].set_orientation("right")
        elif keys[pygame.K_UP] and not character[0].get_orientation() == "bottom":
            character[0].set_orientation("top")
        elif keys[pygame.K_DOWN] and not character[0].get_orientation() == "top":
            character[0].set_orientation("bottom")

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
