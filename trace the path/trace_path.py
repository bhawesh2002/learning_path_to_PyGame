from cmath import e
import sys
import pygame
from pygame.locals import *

pygame.init()

width,height = 800,600
window = pygame.display.set_mode((width,height))
dimensions = window.get_rect()
x_pos = dimensions.centerx
y_pos = dimensions.centery
radius = 25
while True:
    window.fill((0,0,0))
    ball = pygame.draw.circle(window,(22,255,22),(x_pos,y_pos),radius)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()
    if(pygame.key.get_pressed()[K_RIGHT]):
        if(x_pos < dimensions.topright[0] - radius):
            x_pos += 1
        else:
            x_pos = dimensions.topright[0] - radius
    if(pygame.key.get_pressed()[K_LEFT]):
        if(x_pos > dimensions.topleft[0] + radius):
            x_pos -= 1
        else:
            x_pos = dimensions.topleft[0] + radius
    if(pygame.key.get_pressed()[K_UP]):
        if(y_pos > dimensions.topleft[1] + radius):
            y_pos -= 1
        else:
            y_pos = dimensions.topleft[1] +radius
    if(pygame.key.get_pressed()[K_DOWN]):
        if(y_pos < dimensions.bottomleft[1] - radius):
            y_pos += 1
        else:
            y_pos = dimensions.bottomleft[1] - radius
    print(ball.centerx,",",ball.centery)