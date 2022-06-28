import sys
import pygame
from pygame.locals import *

pygame.init()

width,height = 800,600
window = pygame.display.set_mode((width,height))
dimensions = window.get_rect()

while True:
    window.fill((0,0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN or pygame.key == K_q):
            pygame.quit()
            sys.exit()