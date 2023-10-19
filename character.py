import pygame
from constants import SIDE, BLUE, BLACK


class Head:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.orientation = "right"

    def draw(self):
        center_x, center_y = self.x + (SIDE // 2), self.y + (SIDE // 2)
        eye_radius = 5
        eye_padding = 10

        pygame.draw.circle(self.win, BLUE, (center_x, center_y), SIDE // 2)
        match self.orientation:
            case "right":
                pygame.draw.rect(self.win, BLUE, (self.x, self.y, (SIDE // 2), SIDE))
                # left eye
                pygame.draw.circle(
                    self.win,
                    BLACK,
                    (self.x + (SIDE * 3 / 4), self.y + (SIDE // 2) + eye_padding),
                    eye_radius,
                )
                # right eye
                pygame.draw.circle(
                    self.win,
                    BLACK,
                    (self.x + (SIDE * 3 / 4), self.y + (SIDE // 2) - eye_padding),
                    eye_radius,
                )
            case "left":
                pygame.draw.rect(
                    self.win, BLUE, (self.x + (SIDE // 2), self.y, (SIDE // 2), SIDE)
                )
                # left eye
                pygame.draw.circle(
                    self.win,
                    BLACK,
                    (self.x + (SIDE / 4), self.y + (SIDE // 2) + eye_padding),
                    eye_radius,
                )
                # right eye
                pygame.draw.circle(
                    self.win,
                    BLACK,
                    (self.x + (SIDE / 4), self.y + (SIDE // 2) - eye_padding),
                    eye_radius,
                )
            case "top":
                pygame.draw.rect(
                    self.win, BLUE, (self.x, self.y + (SIDE // 2), SIDE, (SIDE // 2))
                )
                # left eye
                pygame.draw.circle(
                    self.win,
                    BLACK,
                    (self.x + (SIDE // 2) - eye_padding, self.y + (SIDE / 4)),
                    eye_radius,
                )
                # right eye
                pygame.draw.circle(
                    self.win,
                    BLACK,
                    (self.x + (SIDE // 2) + eye_padding, self.y + (SIDE / 4)),
                    eye_radius,
                )
            case "bottom":
                pygame.draw.rect(self.win, BLUE, (self.x, self.y, SIDE, (SIDE // 2)))
                # left eye
                pygame.draw.circle(
                    self.win,
                    BLACK,
                    (self.x + (SIDE // 2) - eye_padding, self.y + (SIDE * 3 / 4)),
                    eye_radius,
                )
                # right eye
                pygame.draw.circle(
                    self.win,
                    BLACK,
                    (self.x + (SIDE // 2) + eye_padding, self.y + (SIDE * 3 / 4)),
                    eye_radius,
                )
            case _:
                # For some reason, the orientation is not set.
                pygame.draw.rect(self.win, BLACK, (self.x, self.y, SIDE, SIDE))


class Body:
    def __init__(self, x, y, link):
        self.x = x
        self.y = y
        # link refers to the object ahead of this object
        self.link = link
        self.is_tail = False

    def change_to_tail(self):
        self.is_tail = True

    def draw():
        pass
