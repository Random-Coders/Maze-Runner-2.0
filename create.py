import pygame
import time
import random
from settings import *
from maps import *

def level(display_surface, level, camera, playerx, playery):
    # Rendering involves a little conversion of level coordinates to surface coordinates
    # The active area makes sure only blocks that are shown on screen are rendered

    for y in range(level.levelHeight):
        for x in range(level.levelWidth):
            blockRect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)

            if camera.colliderect(blockRect):
                if tilemap[y][x] == 1:
                    continue
                elif tilemap[y][x] == 0:
                    display_surface.blit(display_surface,(playerx,playery))
                else:
                    pass
