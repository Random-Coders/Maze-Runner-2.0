import pygame
from pygame.locals import *
from settings import *

class Camera(pygame.Rect):
    def __init__(self, targetRect, windowWidth, windowHeight):
        super(Camera,self).__init__(targetRect.rect.x-(windowWidth/2),
                                    targetRect.rect.y-(windowHeight/2),
                                    windowWidth, windowHeight)
        self.cameraxposition = 80
        self.camerayposition = 60

    def update(self, rect, level):
        if rect.x - rect.x > self.cameraxposition:
            self.left = rect.x + self.cameraxposition - self.width/2
        elif rect.x - self.rect.x > self.cameraxposition:
            self.left = rect.x - self.cameraxposition - self.width/2
        if rect.y - rect.y > self.camerayposition:
            self.top = rect.y + self.camerayposition - self.height/2
        elif rect.y - self.rect.y > self.camerayposition:
            self.top = rect.y - self.camerayposition - self.height/2

        # This keeps the camera within the boundaries of the level
        if self.right > level.rightEdge - TILESIZE:
            self.right = level.rightEdge - TILESIZE
        elif self.left < TILESIZE:
            self.left = TILESIZE
        if self.top < TILESIZE*3:
            self.top = TILESIZE*3
        elif self.bottom > level.bottomEdge:
            self.bottom = level.bottomEdge

        return self
