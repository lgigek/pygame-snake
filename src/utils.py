import random


def generate_random_position():
    # random.randint(0, 590) -> 438
    # 438//10 -> 43
    # 43 * 10 -> 430
    # 438 -> 430

    x = random.randint(0, 590) // 10 * 10
    y = random.randint(0, 590) // 10 * 10

    return x, y


def have_collided(cell_1, cell_2):
    return (cell_1[0] == cell_2[0]) and (cell_1[1] == cell_2[1])
