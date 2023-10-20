import pygame
from constants import WIDTH, HEIGHT, FPS, ROWS, COLS, SIDE, GAME_FONT, SCORE_FONT
from board import Board, Apple
from character import Head, Body
import random


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.board = Board(self.win)

        self.character = []
        self.starting_x, self.starting_y = SIDE * 6, SIDE * 7

        self.apple = Apple(self.win)

        self.start_game_text = GAME_FONT.render("Press SPACE To Start", 1, "white")
        self.game_over_text1 = GAME_FONT.render("Game Over...", 1, "white")
        self.game_over_text2 = GAME_FONT.render("Press SPACE To Restart", 1, "white")

        self.score = 0
        self.score_text = SCORE_FONT.render(f"{self.score}", 1, "white")

    def initialize_character(self):
        self.character.append(Head(self.win, self.starting_x, self.starting_y))
        self.character.append(Body(self.win, self.character[-1]))
        self.character.append(Body(self.win, self.character[-1]))

    def reset_game(self):
        self.board = Board(self.win)

        self.character = []
        self.starting_x, self.starting_y = SIDE * 6, SIDE * 7

        self.apple = Apple(self.win)
        self.move_apple()

        self.score = 0

        self.initialize_character()

    def start_game(self):
        run = True
        start_game = False

        self.reset_game()

        self.update_game()
        self.win.blit(
            self.start_game_text,
            (
                WIDTH // 2 - self.start_game_text.get_width() // 2,
                HEIGHT // 2 - self.start_game_text.get_height() // 2,
            ),
        )
        pygame.display.update()

        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    start_game = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                run = False
                start_game = True

        if start_game:
            self.run_game()
        else:
            pygame.quit()

    def run_game(self):
        run = True

        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            self.player_input()

            self.update_game()

            if self.check_collsion():
                run = False
                break

        self.game_over()

    def game_over(self):
        run = True
        start_game = False

        self.win.blit(
            self.game_over_text1,
            (
                WIDTH // 2 - self.game_over_text1.get_width() // 2,
                HEIGHT // 2 - self.game_over_text1.get_height(),
            ),
        )
        self.win.blit(
            self.game_over_text2,
            (
                WIDTH // 2 - self.game_over_text2.get_width() // 2,
                HEIGHT // 2 + self.game_over_text2.get_height() - 30,
            ),
        )
        pygame.display.update()

        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    start_game = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                run = False
                start_game = True

        if start_game:
            self.reset_game()
            self.run_game()
        else:
            pygame.quit()

    def update_game(self):
        self.board.create_board()

        self.apple.draw()

        self.character[-2].make_body()
        self.character[-1].make_tail()

        for i in reversed(range(len(self.character))):
            self.character[i].move()
            self.character[i].draw()

        self.win.blit(self.score_text, (10, 10))

        pygame.display.update()

    def check_collsion(self):
        # Check if head goes beyond the boundaries.
        if self.character[0].get_x() < 0 or self.character[0].get_x() >= WIDTH:
            return True
        elif self.character[0].get_y() < 0 or self.character[0].get_y() >= HEIGHT:
            return True

        # Check for head collsion with body or tail.
        for i in range(1, len(self.character)):
            if (
                self.character[0].get_x() == self.character[i].get_x()
                and self.character[0].get_y() == self.character[i].get_y()
            ):
                return True

        # Check if head hits the apple.
        if (
            self.character[0].get_x() == self.apple.get_x()
            and self.character[0].get_y() == self.apple.get_y()
        ):
            self.score += 1
            self.character.append(Body(self.win, self.character[-1]))
            self.move_apple()

        return False

    def move_apple(self):
        available_positions = self.get_empty_positions()

        if len(available_positions) > 0:
            self.apple.set_position(available_positions.pop())

    def get_empty_positions(self):
        positions = set()
        for i in range(ROWS):
            for j in range(COLS):
                positions.add((i * SIDE, j * SIDE))

        player_position = set()
        for body in self.character:
            player_position.add((body.get_x(), body.get_y()))

        return positions.difference(player_position)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not self.character[0].get_orientation() == "right":
            self.character[0].set_orientation("left")
        elif keys[pygame.K_RIGHT] and not self.character[0].get_orientation() == "left":
            self.character[0].set_orientation("right")
        elif keys[pygame.K_UP] and not self.character[0].get_orientation() == "bottom":
            self.character[0].set_orientation("top")
        elif keys[pygame.K_DOWN] and not self.character[0].get_orientation() == "top":
            self.character[0].set_orientation("bottom")
