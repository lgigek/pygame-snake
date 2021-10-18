import random

import pygame
from pygame.locals import *

# pygame stuff
from src.apple import Apple
from src.utils import generate_random_position
from src.utils import have_collided

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# snake direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# snake properties
snake_position = [(200, 200), (210, 200), (220, 200)]  # initial position
snake_body = pygame.Surface((10, 10))  # defining body type
snake_body.fill((255, 255, 255))  # setting a color to snake_body
snake_direction = RIGHT  # setting a default direction

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
                snake_direction = UP
            if event.key == K_DOWN:
                snake_direction = DOWN
            if event.key == K_LEFT:
                snake_direction = LEFT
            if event.key == K_RIGHT:
                snake_direction = RIGHT

    # moves the snake's head according to its direction
    if snake_direction == UP:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] - 10)
    if snake_direction == DOWN:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] + 10)
    if snake_direction == LEFT:
        snake_position[0] = (snake_position[0][0] - 10, snake_position[0][1])
    if snake_direction == RIGHT:
        snake_position[0] = (snake_position[0][0] + 10, snake_position[0][1])

    # checking if snake's head and apple have collided
    if have_collided(snake_position[0], apple.position):
        apple = Apple()
        snake_position.append((0, 0))  # increase snake

    # makes the snake move forward
    for i in range(len(snake_position) - 1, 0, -1):
        snake_position[i] = (snake_position[i - 1][0], snake_position[i - 1][1])

    # "cleans" the screen
    screen.fill((0, 0, 0))

    # printing apple
    screen.blit(apple.body, apple.position)

    # "printing" the snake_body for each snake_position
    for position in snake_position:
        screen.blit(snake_body, position)

    pygame.display.update()
