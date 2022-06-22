from asyncio.windows_events import NULL
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


def draw_screen(xpos, ypos, sizex=100, sizey=100):
    ballon_resized = pygame.transform.scale(ballon, (sizex, sizey))
    window.fill((255, 255, 255))
    window.blit(ballon_resized, (xpos, ypos))
    pygame.display.update()
    # The full screen update is done using pygame.display.flip().
    pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    clock.tick(60)
    xpos = 100
    ypos = 100
    sizex, sizey = 100, 100
    while(True):
        for event in pygame.event.get():
            # if the user wants to quit either click cross or press 'q'
            if (event.type == QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_LEFT]:  # move to left
            if xpos == 0:
                NULL
            else:
                xpos -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:  # move to right
            if xpos == 700:
                NULL
            else:
                xpos += 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:  # move down
            if ypos == 500:
                NULL
            else:
                ypos += 1
        if pygame.key.get_pressed()[pygame.K_UP]:  # move up
            if ypos == 0:
                NULL
            else:
                ypos -= 1
        if pygame.key.get_pressed()[pygame.K_m]:  # decrease size
            if sizex == 0 and sizey == 0:
                NULL
            else:
                sizex -= 1
                sizey -= 1
        if pygame.key.get_pressed()[pygame.K_p]:  # increase size
            if sizex == 500 and sizey == 500:
                NULL
            else:
                sizex += 1
                sizey += 1
        draw_screen(xpos, ypos, sizex, sizey)


if __name__ == '__main__':
    main()
