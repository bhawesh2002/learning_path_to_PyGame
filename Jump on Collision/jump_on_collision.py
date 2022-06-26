import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height, width = 600, 800

window = pygame.display.set_mode((width, height))
mouse = pygame.image.load(os.path.join('Jump on Collision', 'Assets', 'mouse.png')).convert()
mouse_scaled = pygame.transform.scale(mouse,(150,100))
while True:
    x_pos, y_pos = 0,490
    pygame.display.update()
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()
    window.fill((255,255,255))
    window.blit(mouse_scaled,(x_pos,y_pos))