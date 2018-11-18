# Import Pygame
import pygame
# Import loading code for pygame
from pygame.locals import *
from Sprite import Bird
# Tile Value Constants
DIRT = 0
GRASS = 1
WATER = 2
LEAVE = 3

# Color Constants in RGB
BROWN = (99, 59, 30)
GREEN = (69, 122, 67)
LIGHTGREEN = (111, 206, 107)
BLUE = (50, 178, 229)
GRAY = (151, 152, 153)
WHITE = (255, 255, 255)
RED = (193, 44, 44)

# Pair tiles with color
textures = {
            DIRT  : BROWN,
            GRASS : GREEN,
            WATER : BLUE,
            LEAVE : LIGHTGREEN,
        }

# Create Tile Map
tilemap = [
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, GRASS, GRASS],
          ]

# Create Map
TILESIZE = 50
MAPWIDTH = 15
MAPHEIGHT = 15

# Initialise Pygame
pygame.init()

# Create window
display_surface = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPWIDTH*TILESIZE))

# Create display title
pygame.display.set_caption('Hand Game')

bird = Bird()

# MAIN LOOP
while True:

    # If game quit than quit app
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    bird.handle_keys() # handle the keys
    bird.draw(display_surface)

    # Update display
    pygame.display.update()
