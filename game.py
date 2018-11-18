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
# Import level
import level
# Import camera
import camera
# Import Create
import create
# Initialise Pygame
pygame.init()

# Create window
display_surface = pygame.display.set_mode((750,750))

# Create display title
pygame.display.set_caption('Hand Game')

# create player
player = Player()

# Fill base black backgound
display_surface.fill((0, 0, 0))

# Create rect
rect = pygame.Rect(750,750,60,90)

# Create camera
camera = camera.Camera(rect, MAPWIDTH, MAPHEIGHT)

# Only Allow Script that only allows python3.6 and directly called script
if __name__ != '__main__':
    # Python version not 3.6
    print("Must be using Python 3.6")
    exit()

recognizer = gr.GestureRecognizer(print_pos=False)
recognizer.start_recognizing()

current = level.Level("level_1.lvl")

# MAIN LOOP
while True:
    time.sleep(1./60)

    create.level(display_surface, current, camera)

    # bird.handle_keys() # handle the keys
    x_dir = recognizer.gesture.x_dir
    y_dir = recognizer.gesture.y_dir
    player.handle_gestures(x_dir, y_dir)
    player.draw(display_surface)

    camera.update(rect, current)

    # Update display
    pygame.display.update()
