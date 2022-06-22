import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height = 800
width = 600
window = pygame.display.set_mode((height, width))
window.fill((255, 255, 255))


def main():
    while(True):
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
