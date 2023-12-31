import pygame
from constants import SIDE, BLUE, BLACK


class Head:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.orientation = "right"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_orientation(self):
        return self.orientation

    def set_orientation(self, direction):
        self.orientation = direction

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

    def move(self):
        match self.orientation:
            case "right":
                self.x += SIDE
            case "left":
                self.x -= SIDE
            case "top":
                self.y -= SIDE
            case "bottom":
                self.y += SIDE
            case _:
                self.x = 0
                self.y = 0


class Body:
    def __init__(self, win, link):
        self.win = win
        # link refers to the object ahead of this object
        self.link = link
        self.x = -50
        self.y = -50
        self.orientation = "right"
        self.is_tail = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_orientation(self):
        return self.orientation

    def make_tail(self):
        self.is_tail = True

    def make_body(self):
        self.is_tail = False

    def draw(self):
        if self.is_tail:
            center_x, center_y = self.x + (SIDE // 2), self.y + (SIDE // 2)

            pygame.draw.circle(self.win, BLUE, (center_x, center_y), SIDE // 2)
            match self.orientation:
                case "left":
                    pygame.draw.rect(
                        self.win, BLUE, (self.x, self.y, (SIDE // 2), SIDE)
                    )
                case "right":
                    pygame.draw.rect(
                        self.win,
                        BLUE,
                        (self.x + (SIDE // 2), self.y, (SIDE // 2), SIDE),
                    )
                case "bottom":
                    pygame.draw.rect(
                        self.win,
                        BLUE,
                        (self.x, self.y + (SIDE // 2), SIDE, (SIDE // 2)),
                    )
                case "top":
                    pygame.draw.rect(
                        self.win, BLUE, (self.x, self.y, SIDE, (SIDE // 2))
                    )
                case _:
                    # For some reason, the orientation is not set.
                    pygame.draw.rect(self.win, BLACK, (self.x, self.y, SIDE, SIDE))
        else:
            pygame.draw.rect(self.win, BLUE, (self.x, self.y, SIDE, SIDE))

    def move(self):
        self.x = self.link.get_x()
        self.y = self.link.get_y()
        self.orientation = self.link.get_orientation()
