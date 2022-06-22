import sys  # for sys.exit()
import os
from turtle import width  # for os.path.isfile()
import pygame  # for pygame.init()
from pygame.locals import *  # import the locals from the pygame module

pygame.init()

height = 800
width = 600
window = pygame.display.set_mode((height, width))


def draw_screen():
    window.fill((255, 255, 255))
    pygame.display.update()


def main():
    while(True):
        for event in pygame.event.get():
            # if the user wants to quit either click cross or press 'q'
            if (event.type == QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()
        draw_screen()


if __name__ == '__main__':
    main()
