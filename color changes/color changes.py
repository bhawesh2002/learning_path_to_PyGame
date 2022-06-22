from asyncio.windows_events import NULL
import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height = 800
width = 600
window = pygame.display.set_mode((height, width))
beach_ball = pygame.image.load(os.path.join(
    "color changes", "Assets", "beach-ball.jpg"))


def draw_screen(xpos, ypos, sizex=150, sizey=150):
    window.fill((255, 255, 255))
    beach_ball_resized = pygame.transform.scale(beach_ball, (150, 150))
    window.blit(beach_ball_resized, (xpos, ypos))


def main():
    xpos = 100
    ypos = 100
    while(True):
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if xpos == 0:
                NULL
            else:
                xpos -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if xpos == 600:
                NULL
            else:
                xpos += 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if ypos == 500:
                NULL
            else:
                ypos += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            if ypos == 0:
                NULL
            else:
                ypos -= 1

        draw_screen(xpos, ypos)


if __name__ == '__main__':
    main()
