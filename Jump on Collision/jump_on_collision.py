import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height, width = 600, 800
velocity = 5
clock = pygame.time.Clock()
window = pygame.display.set_mode((width, height))
mouse = pygame.image.load(os.path.join('Jump on Collision', 'Assets', 'mouse.png')).convert()
mouse_scaled = pygame.transform.scale(mouse,(150,100))
mouse_scaled.set_colorkey((255,255,255))
x_pos, y_pos = 0,490
font = pygame.font.SysFont('Arial', 50)
collide = font.render('Collision!', True, (255, 0, 0))
reached = font.render('Reached!', True, (0, 255, 0))
obj = pygame.draw.circle(window, (255,0,0), (400,550), 50)
pygame.display.flip()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()
    window.fill((255,255,255))
    obj = pygame.draw.circle(window, (255,0,0), (400,550), 50)
    window.blit(mouse_scaled,(x_pos,y_pos))
    pygame.display.flip()
    if (pygame.key.get_pressed()[pygame.K_RIGHT]):
        if(x_pos < 650):
            x_pos += velocity
            if(x_pos >= (obj.left - 150) and x_pos <= (obj.right - 150)):
                if(y_pos > 420):
                    window.blit(collide, (350, height/2))
                    x_pos = obj.left - 150
                    pygame.display.update()
        else:
            window.blit(reached, (350, height/2))
            x_pos = 650
            pygame.display.update()
    if(pygame.key.get_pressed()[K_LEFT]):
        if(x_pos > 0):
            x_pos -= velocity
            if(x_pos <=obj.right and x_pos >= obj.left):
                if(y_pos > 420):
                    window.blit(collide, (350, height/2))
                    x_pos = obj.right
                    pygame.display.update()
        else:
            x_pos = 0
    if(y_pos >= 0):
        if(y_pos <= 490):
            y_pos += 3
        if(pygame.key.get_pressed()[K_UP]):
            if(y_pos > 200):
                y_pos -= velocity
            else:
                y_pos = 200