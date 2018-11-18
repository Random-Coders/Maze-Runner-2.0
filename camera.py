import pygame
from pygame.locals import *
from settings import *

class Camera(pygame.Rect):
    cameraxposition = 80
    camerayposition = 60
    def __init__(self, targetRect, windowWidth, windowHeight):
        super(Camera,self).__init__(targetRect.centerx-(windowWidth/2),
                                    targetRect.centery-(windowHeight/2),
                                    windowWidth, windowHeight)

    def update(self, rect, level):
        if self.centerx - rect.centerx > self.cameraxposition:
            self.left = rect.centerx + self.cameraxposition - self.width/2
        elif rect.centerx - self.centerx > self.cameraxposition:
            self.left = rect.centerx - self.cameraxposition - self.width/2
        if self.centery - rect.centery > self.camerayposition:
            self.top = rect.centery + self.camerayposition - self.height/2
        elif rect.centery - self.centery > self.camerayposition:
            self.top = rect.centery - self.camerayposition - self.height/2

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
