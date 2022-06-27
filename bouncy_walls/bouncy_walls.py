import sys #for sys.exit()
import os  #for os.path.join()
import pygame #import the pygame module
from pygame.locals import *  #import the pygame.locals for easier access to key presses and mouse positions

pygame.init()

width,height = 800,600

window = pygame.display.set_mode((width,height))
dimensions = window.get_rect()
x_pos = 400
y_pos = 0
while True:
    window.fill((255,255,255))
    ball = pygame.draw.circle(window,(22,255,22),(x_pos,y_pos),25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()
    if(pygame.key.get_pressed()[K_RIGHT]):
        if(x_pos < dimensions.width):
            x_pos += 1
        else:
            x_pos = dimensions.width