import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height, width = 600, 800
velocity = 3
window = pygame.display.set_mode((width, height))
mouse = pygame.image.load(os.path.join('Jump on Collision', 'Assets', 'mouse.png')).convert()
mouse_scaled = pygame.transform.scale(mouse,(150,100))
x_pos, y_pos = 0,490
while True:
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()
    if (pygame.key.get_pressed()[pygame.K_RIGHT]):
        if(x_pos < 650):
            x_pos += velocity
        else:
            x_pos = 650
    if(pygame.key.get_pressed()[K_LEFT]):
        if(x_pos > 0):
            x_pos -= velocity
        else:
            x_pos = 0
    if(y_pos >= 0):
        if(y_pos <= 490):
            y_pos += 1
        if(pygame.key.get_pressed()[K_UP]):
            print(y_pos)
            if(y_pos > 200):
                y_pos -= velocity
            else:
                y_pos = 200
    window.fill((255,255,255))
    window.blit(mouse_scaled,(x_pos,y_pos))
    pygame.display.update()