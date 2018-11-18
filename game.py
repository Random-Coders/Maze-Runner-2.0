# Import Pygame
import pygame
# Import loading code for pygame
from pygame.locals import *

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
colors = {
            DIRT  : BROWN,
            GRASS : GREEN,
            WATER : BLUE,
            LEAVE : LIGHTGREEN
        }

# Create Tile Map
tilemap = [
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, LEAVE, WATER],
            [GRASS, GRASS, GRASS]
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

# MAIN LOOP
while True:

    # If game quit than quit app
    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()
            exit()

    # Update display
    pygame.display.update()

character = makeSprite("blue.png")
showSprite(character)
character, x, 800)
xPo = 500
yPo = 500
xSpeed = 0
ySpeed = 0
moveSprite(character, xPo, yPo)
while True:
    if keyPressed("up"):
        rotateSprite(character, 0)
        ySpeed -= 2
    elif keyPressed("down"):
        rotateSprite(character, 200)
        ySpeed += 2
    elif keyPressed("right"):
        rotateSprite(character, 200)
        xSpeed += 2
    elif keyPressed("left"):
        rotateSprite(character, -200)
        xSpeed -= 2
    xPo += xSpeed
    if xPo > 980:
        xPo = -100
    elif xPo < -100
        xPo = 980

    yPo += ySpeed
    if yPo > 900:
        yPo = -100
    elif yPo < -100:
        yPo = 900
    moveSprite(character, xPo, yPo)
    tick(25)
