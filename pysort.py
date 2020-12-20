
# -------------------------------------------------------imports------------------------------------------------------------ #
import pygame
from pygame.draw import rect, line
from pygame.time import Clock
from random import randint

# ---------------------------------------------------global variables------------------------------------------------------- #
width = 600
height = 400
rez = 10
rows = height // rez
cols = width // rez
display = pygame.display.set_mode((width, height))

array = []
for i in range(width // rez):
    array.append(randint(1, height // rez))

# -----------------------------------------------------draw functions------------------------------------------------------- #


def drawgrid():
    for i in range(rez, width, rez):
        for j in range(rez, height, rez):
            line(display, (0, 0, 0), (i, 0), (i, height))
            line(display, (0, 0, 0), (0, j), (width, j))


def draw(n=None):
    for i in range(len(array)):
        for j in range(array[i]):
            rect(display, (0, 128, 128), (i * rez, (rows - j - 1) * rez, rez, rez))

    if n:
        for j in range(array[n]):
            rect(display, (100, 170, 190),
                 (n * rez, (rows - j - 1) * rez, rez, rez))

    drawgrid()

# ---------------------------------------swapping function to swap to elements in a array---------------------------------- #


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# -------------------------------------------------------the main loop------------------------------------------------------ #


def main():
    n = len(array)
    print(n)
    run = True
    clock = Clock()
    i = 0
    j = 0

    while run:
        clock.tick(60)
        display.fill((220, 220, 220))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:

        if array[j] > array[j + 1]:
            swap(array, j, j + 1)
            # draw()
            # pygame.display.flip()

        j += 1

        if i > n - 1:
            for k in range(len(array)):
                array[k] = randint(1, height // rez)

            i = 0
            j = 0

        if j >= n - 1 - i:
            j = 0
            i += 1

        draw(j)
        pygame.display.flip()

# -------------------------------------------------calling the function---------------------------------------------------- #


if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------------------------------------------------------- #
