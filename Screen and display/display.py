import sys # for sys.exit()
import pygame # for pygame.init()
from pygame.locals import * #import the locals from the pygame module

pygame.init()

height = 800
width = 600

while(True):
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()