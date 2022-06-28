import sys
import pygame
from pygame.locals import *

pygame.init()

width, height = 800, 600

window = pygame.display.set_mode((width, height))
dimensions = window.get_rect()
x_pos = dimensions.centerx
y_pos = dimensions.centery
counter = 3
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()
    if(y_pos < dimensions.bottomleft[1] - 25):
        while(y_pos <= dimensions.bottomleft[1] - 25):
            y_pos += 0.5
            window.fill((0, 0, 0))
            obj = pygame.draw.circle(window, (22, 225, 22), (x_pos, y_pos), 25)
            pygame.display.update()
        if(y_pos >= dimensions.bottomleft[1] - 25):
            counter -= 1
            while(y_pos >= dimensions.bottomleft[1] - 200):
                y_pos -= 0.3
                window.fill((0, 0, 0))
                obj = pygame.draw.circle(
                    window, (22, 225, 22), (x_pos, y_pos), 25)
                pygame.display.update()
    pygame.display.update()
