# Import Pygame
import pygame
# Import sys
import sys
# Import loading code for pygame
from pygame.locals import *
from Sprite import Bird
# Tile Value Constants
WALL = 0
GROUND = 1
WATER = 2

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
            WALL  : BROWN,
            GROUND : GREEN,
            WATER : BLUE
        }

# Create Tile Map
tilemap = [
            [WALL, WALL,   WALL,   WALL,   WALL],
            [WALL, GROUND, GROUND, GROUND, WALL],
            [WALL, GROUND, WALL,   GROUND, WALL],
            [WALL, GROUND, WALL,   GROUND, WALL],
            [WALL, GROUND, WALL,   GROUND, WALL]
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
# Only Allow Script that only allows python3.6 and directly called script
if sys.version_info[0] == 3.6 or __name__ == '__main__':
    # Python version not 3.6
    print("Must be using Python 3.6")
    exit()

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
