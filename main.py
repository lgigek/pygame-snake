import random

import pygame
from pygame.locals import *

from src.apple import Apple
from src.snake import Direction
from src.snake import Snake
from src.utils import have_collided

# pygame stuff
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

snake = Snake()

# apple properties
apple = Apple()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # capture user inputs and set snake's direction
        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake.direction = Direction.UP
            if event.key == K_DOWN:
                snake.direction = Direction.DOWN
            if event.key == K_LEFT:
                snake.direction = Direction.LEFT
            if event.key == K_RIGHT:
                snake.direction = Direction.RIGHT

    snake.move()

    # checking if snake's head and apple have collided
    if have_collided(snake.head, apple.position):
        apple = Apple()
        snake.add_tail()

    # "cleans" the screen
    screen.fill((0, 0, 0))

    # printing apple
    screen.blit(apple.body, apple.position)

    # "printing" the snake_body for each snake_position
    for position in snake.position:
        screen.blit(snake.body, position)

    pygame.display.update()
