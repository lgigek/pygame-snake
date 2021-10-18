from enum import Enum

import pygame


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def is_opposite(direction_1, direction_2) -> bool:
        if direction_1 == Direction.UP and direction_2 == Direction.DOWN:
            return True
        if direction_1 == Direction.DOWN and direction_2 == Direction.UP:
            return True
        if direction_1 == Direction.LEFT and direction_2 == Direction.RIGHT:
            return True
        if direction_1 == Direction.RIGHT and direction_2 == Direction.LEFT:
            return True
        return False


class Snake:
    def __init__(self):
        # snake properties
        self.position = [(200, 200), (210, 200), (220, 200)]  # setting initial position
        self.body = pygame.Surface((10, 10))  # defining body type
        self.body.fill((255, 255, 255))  # setting a color to snake_body
        self._direction = Direction.RIGHT  # setting a default direction

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, new_value: Direction):
        if not Direction.is_opposite(self._direction, new_value):
            self._direction = new_value

    @property
    def head(self):
        return self.position[0]

    def move(self):
        if self.direction == Direction.UP:
            self.position[0] = (self.position[0][0], self.position[0][1] - 10)
        if self.direction == Direction.DOWN:
            self.position[0] = (self.position[0][0], self.position[0][1] + 10)
        if self.direction == Direction.LEFT:
            self.position[0] = (self.position[0][0] - 10, self.position[0][1])
        if self.direction == Direction.RIGHT:
            self.position[0] = (self.position[0][0] + 10, self.position[0][1])

        # makes the snake move forward
        for i in range(len(self.position) - 1, 0, -1):
            self.position[i] = (self.position[i - 1][0], self.position[i - 1][1])

    def add_tail(self):
        self.position.append(self.position[len(self.position) - 1])
