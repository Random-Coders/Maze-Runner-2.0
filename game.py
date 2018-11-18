# Import Pygame
import pygame
# Import time
import time
# Import loading code for pygame
from pygame.locals import *
from Sprite import Player
from gesture_recognizer import GestureRecognizer as gr
# Import settings
from settings import *
# Import maps
from maps import *
# Import os
import os

# Initialise Pygame
pygame.init()

# Create window
display_surface = pygame.display.set_mode((750,750))

# Create display title
pygame.display.set_caption('Hand Game')

player = Player()
# Only Allow Script that only allows python3.6 and directly called script
if __name__ != '__main__':
    # Python version not 3.6
    print("Must be using Python 3.6")
    exit()

recognizer = gr.GestureRecognizer(print_pos=False)
recognizer.start_recognizing()

# MAIN LOOP
while True:
    time.sleep(1./60)
    # If game quit than quit app
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            os.remove('__pycache__/Sprite.cpython-36.pyc')
            exit()

    for row in range(MAPHEIGHT):

        for column in range(MAPWIDTH):
            pygame.draw.rect(display_surface, colors[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

    # bird.handle_keys() # handle the keys
    x_dir = recognizer.gesture.x_dir
    y_dir = recognizer.gesture.y_dir
    player.handle_gestures(x_dir, y_dir)
    player.draw(display_surface)

    # Update display
    pygame.display.update()
