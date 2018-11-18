import pygame

from pygame.locals import *

DIRT = 0
GRASS = 1
WATER = 2
LEAVE = 3

BROWN =
GREEN =
LIGHTGREEN =
BLUE =

colors = {
            DIRT  : BROWN,
            GRASS : GREEN
            WATER : BLUE
            LEAVE : LIGHTGREEN
        }

tilemap = [
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, GRASS, GRASS]
          ]

TILESIZE = 50
MAPWIDTH = 15
MAPHEIGHT = 15

pygame.init()

display_surface = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPWIDTH*TILESIZE))

pygame.display.set_caption('Hand Game')

while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()
            exit()

    pygame.display.update()
