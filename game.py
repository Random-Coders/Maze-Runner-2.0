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
            DIRT  : BROWN
            GRASS : GREEN
            WATER : BLUE
            LEAF : LIGHTGREEN
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
