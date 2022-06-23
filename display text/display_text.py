import sys
import pygame

from pygame.locals import *

pygame.init()

height = 800
width = 600

window = pygame.display.set_mode((height, width), pygame.RESIZABLE)


def main():
    window.fill((255, 255, 255))
    pygame.display.update()


if __name__ == "__main__":
    main()
