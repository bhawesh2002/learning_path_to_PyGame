import sys
import pygame
from pygame.locals import *

pygame.init()

height = 600
width = 800

window = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("Coordinate System")

def draw_screen():
    window.fill((255,255,255))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    clock.tick(60)
    while(True):
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()
            draw_screen()




if __name__ == '__main__':
    main()