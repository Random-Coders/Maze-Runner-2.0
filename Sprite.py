#background movement for game
import pygame
import os
from gesture_recognizer import GestureRecognizer as gr
from settings import *
# import gesture recognizer class
class Player(object):  # represents the character, not the game
    def __init__(self):
        """ The constructor of the class """
        # self.image = pygame.image.load("assets/Circle.png")
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("assets/Circle.png").convert_alpha()
        self.sprite.image = pygame.transform.scale(self.sprite.image, (30,30))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.move_ip(175,175)
        # self.image = pygame.transform.scale(self.image, (50, 50))
        # the character's position
<<<<<<< HEAD
        self.x = 175
        self.y = 175
        self.prev_x_dir = 175
        self.prev_y_dir = 175
    def handle_keys(self):
=======
        self.prev_x = 0
        self.prev_y = 0
        self.prev_x_dir = 0
        self.prev_y_dir = 0
    def handle_keys(self, list):
        
>>>>>>> 5fa1ea5fb1f6ce299260e5ea5cd63d494ef26521
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]: # down key
            self.sprite.rect.centery += dist # move down
        elif key[pygame.K_UP]: # up key
            self.sprite.rect.centery -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.sprite.rect.centerx += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.sprite.rect.centerx -= dist # move left
        if self.sprite.rect.collidelist(list) > 1:
            print('collided')
            self.sprite.rect.centerx = self.prev_x
            self.sprite.rect.centery = self.prev_y
        self.prev_x = self.sprite.rect.centerx
        self.prev_y = self.sprite.rect.centery
    def handle_gestures(self, x_dir, y_dir, rect_list):
        dist = 10
        if x_dir == 0 and y_dir == 0:
            # still
            print("still")
        if x_dir > 0.5:
            # moving right
            print("moving right")
            self.sprite.rect.centerx += dist*x_dir
        elif x_dir < 0.5:
            # moving left
            print("moving left")
            self.sprite.rect.centerx -= dist*x_dir
        if y_dir > 0.5:
            # moving up
            print("moving up")
            self.sprite.rect.centery -= dist*y_dir
        elif y_dir < 0.5:
            # moving down
            print("moving down")
            self.sprite.rect.centery += dist*y_dir
        if self.sprite.rect.collidelist(list) > 1:
            print('collided')
            self.sprite.rect.centerx = self.prev_x
            self.sprite.rect.centery = self.prev_y
        self.prev_x_dir = x_dir
        self.prev_y_dir = y_dir
        self.prev_x = self.sprite.rect.centerx
        self.prev_y = self.sprite.rect.centery
        # print('x_dir', x_dir)
        # print('y_dir', y_dir)
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.sprite.image, self.sprite.rect.topleft)
