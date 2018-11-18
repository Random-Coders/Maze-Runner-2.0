import pygame
import time
import random
from settings import *
from maps import *

def level(display_surface, level, camera):
    # Rendering involves a little conversion of level coordinates to surface coordinates
    # The active area makes sure only blocks that are shown on screen are rendered
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(display_surface, colors[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))


    for y in range(level.levelHeight):
        for x in range(level.levelWidth):
            blockRect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)

            if camera.colliderect(blockRect):
                if level.collisionLayer[y][x] == level.blank:
                    continue
                if level.collisionLayer[y][x] == level.block:
                    display_surface.blit(display_surface,
                                 ((x*TILESIZE) - camera.left,
                                 (y*TILESIZE) - camera.top,))
