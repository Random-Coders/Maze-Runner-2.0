import pygame
from settings import *

class Level(object):
    blank = '.'
    block = '0'

    def __init__(self, file):
        self.collisionLayer = [row.strip('\n') for row in\
                          open(file, 'r').readlines()]
        self.levelWidth = len(self.collisionLayer[0])
        self.levelHeight = len(self.collisionLayer)

        self.leftEdge = 0
        self.topEdge = 0
        self.rightEdge = int(self.levelWidth) * TILESIZE
        self.bottomEdge = int(self.levelHeight) * TILESIZE
