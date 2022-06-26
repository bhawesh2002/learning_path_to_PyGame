import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height, width = 600, 800

window = pygame.display.set_mode(width, height)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()
