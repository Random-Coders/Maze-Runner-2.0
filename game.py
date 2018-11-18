# Import Pygame
import pygame
# Import time
import time
# Import loading code for pygame
from pygame.locals import *
from Sprite import Bird
# Import gesture recognizer
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

# Fill base black backgound
display_surface.fill((0, 0, 0))

# Create Sprite
bird = Bird()

# Create rect
rect = pygame.Rect(750,750,60,90)

# Create camera
camera = camera.Camera(rect, MAPWIDTH, MAPHEIGHT)

if __name__ != '__main__':
    # Python version not 3.6
    print("Must be using Python 3.6")
    exit()

recognizer = gr.GestureRecognizer()
recognizer.start_recognizing()

current = level.Level("level_1.lvl")

# MAIN LOOP
while True:
    time.sleep(1./60)
    # If game quit than quit app
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            os.remove('__pycache__/Sprite.cpython-36.pyc')
            exit()

    create.level(display_surface, current, camera)

    bird.handle_keys() # handle the keys
    bird.draw(display_surface)

    camera.update(rect, current)

    # Update display
    pygame.display.update()
