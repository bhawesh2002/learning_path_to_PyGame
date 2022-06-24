import sys
import pygame
from pygame.locals import *

pygame.init()

height = 600
width = 800

window = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("Coordinate System")

def main():
    pygame.display.update()
    while(True):
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit




if __name__ == '__main__':
    main()