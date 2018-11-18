#background movement for game
import pygame
import os
from gesture_recognizer import GestureRecognizer as gr
# import gesture recognizer class
#set hand pos as a variable equal to the object (sprite)
class Bird(object):  # represents the character, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load("blue.png")
        # the character's position
        self.x = 0
        self.y = 0

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))
