#background movement for game :)
import pygame
import os
# import gesture recognizer class
class Player(object):  # represents the character, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load("assets/Circle.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        # the character's position
        self.x = 100
        self.y = 100
        self.prev_x_dir = 0
        self.prev_y_dir = 0
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
        dist = 10
        if x_dir == 0 and y_dir == 0:
            # still
            print("still")
        if x_dir > 0 and x_dir > 0.5:
            # moving right
            print("moving right")
            self.x += dist
        elif x_dir < 0 and x_dir < -0.5:
            # moving left
            print("moving left")
            self.x -= dist
        if y_dir > 0 and y_dir > 0.5:
            # moving up
            print("moving up")
            self.y -= dist
        elif y_dir < 0 and y_dir < -0.5:
            # moving down
            print("moving down")
            self.y += dist
        self.prev_x_dir = x_dir
        self.prev_y_dir = y_dir
        # print('x_dir', x_dir)
        # print('y_dir', y_dir)
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))
