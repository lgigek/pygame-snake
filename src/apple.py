import pygame

from src.utils import generate_random_position


class Apple:
    def __init__(self):
        self.position = generate_random_position()
        self.body = pygame.Surface((10, 10))
        self.body.fill((255, 0, 0))
