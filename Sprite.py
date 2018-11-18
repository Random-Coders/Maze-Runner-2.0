#background movement for game :)
import pygame
import os
# import gesture recognizer class
class Player(object):  # represents the character, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load("assets/Circle.png")
        # the character's position
        self.x = 100
        self.y = 100

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
    def handle_gestures(self, x_dir, y_dir):
        if x_dir == 0 and y_dir == 0:
            print("still")
        if x_dir > 0 and x_dir > 0.5:
            print("moving right")
        elif x_dir < 0 and x_dir < -0.5:
            print("moving left")
        if y_dir > 0 and y_dir > 0.5:
            print("moving up")
        elif y_dir < 0 and y_dir < -0.5:
            print("moving down")
        # print('x_dir', x_dir)
        # print('y_dir', y_dir)
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))
