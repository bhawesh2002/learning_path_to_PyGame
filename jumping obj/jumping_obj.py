import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height = 600
width = 800

window = pygame.display.set_mode((width,height), pygame.RESIZABLE)

while(True):
    window.fill((25,205,14))  # fill the screen with a light green color
    pygame.display.update()
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()