import sys
import os
import pygame
from pygame.locals import *

pygame.init()

width,height = 800,600

window = pygame.display.set_mode((width,height))
dimensions = window.get_rect()
pos = dimensions.midtop
while True:
    window.fill((255,255,255))
    ball = pygame.draw.circle(window,(22,255,22),(pos),25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()