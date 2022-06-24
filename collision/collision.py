import sys
import pygame
from pygame.locals import *

pygame.init()

position = [1000,600]
window  = pygame.display.set_mode(position)
pygame.display.set_caption("Collision")

def main():
    window.fill((255,255,255))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()