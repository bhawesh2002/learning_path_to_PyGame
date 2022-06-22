import sys  # for sys.exit()
import os
from turtle import width  # for os.path.isfile()
import pygame  # for pygame.init()
from pygame.locals import *  # import the locals from the pygame module

pygame.init()

height = 800
width = 600
window = pygame.display.set_mode((height, width))
ballon = pygame.image.load(os.path.join(
    "moving objects", "Assets", "ballon.jpg"))
ballon_resized = pygame.transform.scale(ballon, (100, 100))
pos = xpos, ypos = 100, 100


def draw_screen():
    window.fill((255, 255, 255))
    window.blit(ballon_resized, (pos))
    pygame.display.update()
    # The full screen update is done using pygame.display.flip().
    pygame.display.flip()


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
