# Importing pygame module
import pygame
from pygame.locals import *

class Rectangle:
    #class fields
    # size, color,
    def __init__(self,size,pos,color,thickness,window):
        self.size = size
        self.pos = pos
        self.color = color #tween from the original color to BLACK depending on health
        self.health=100
        self.obj = pygame.draw.rect(window,color,[pos[0],pos[1],size[0],size[1]], thickness)
        self.window=window
        pygame.display.update()

    