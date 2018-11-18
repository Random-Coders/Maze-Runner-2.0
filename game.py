import pygame

from pygame.locals import *

DIRT = 0
GRASS = 1
WATER = 2
LEAVE = 3

BROWN = (99, 59, 30)
GREEN = 69, 122, 67)
LIGHTGREEN = (111, 206, 107)
BLUE = (50, 178, 229)
GRAY = (151, 152, 153)
WHITE = (255, 255, 255)
RED = (193, 44, 44)


colors = {
            DIRT  : BROWN,
            GRASS : GREEN
            WATER : BLUE
            LEAVE : LIGHTGREEN
        }


pygame.init()

display_surface = pygame.display.set_mode((1000,1000))

pygame.display.set_caption('Hand Game')

while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()
            exit()

    pygame.display.update()
