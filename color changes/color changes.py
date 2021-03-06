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
    "color changes", "Assets", "beach-ball.jpg")).convert()


def draw_screen(xpos, ypos, bgd_img, sizex=150, sizey=150):
    beach_ball_resized = pygame.transform.scale(beach_ball, (sizex, sizey))
    beach_ball.set_colorkey((255, 255, 255))
    window.blit(bgd_img, (0, 0))
    window.blit(beach_ball_resized, (xpos, ypos))
    pygame.display.update()
    pygame.display.flip()


def main():
    window.fill((255, 255, 255))
    xpos = 100
    ypos = 100
    sizex = 150
    sizey = 150
    bgd_image = pygame.image.load(os.path.join(
        "color changes", "Assets", "white_screen.jpg")).convert()
    bgd_image_scaled = pygame.transform.scale(bgd_image, (800, 600))
    while(True):
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
        if pygame.key.get_pressed()[pygame.K_m]:
            if sizex == 0 and sizey == 0:
                NULL
            else:
                sizex -= 1
                sizey -= 1
        if pygame.key.get_pressed()[pygame.K_p]:
            if sizex == 600 and sizey == 600:
                NULL
            else:
                sizex += 1
                sizey += 1
        if(pygame.key.get_pressed()[pygame.K_y]):
            bgd_image = pygame.image.load(os.path.join(
                "color changes", "Assets", "yellow_screen.jpg"))
            bgd_image_scaled = pygame.transform.scale(bgd_image, (800, 600))
        if(pygame.key.get_pressed()[pygame.K_r]):
            bgd_image = pygame.image.load(os.path.join(
                "color changes", "Assets", "red_screen.jpg"))
            bgd_image_scaled = pygame.transform.scale(bgd_image, (800, 600))
        if(pygame.key.get_pressed()[pygame.K_b]):
            bgd_image = pygame.image.load(os.path.join(
                "color changes", "Assets", "blue_screen.jpg"))
            bgd_image_scaled = pygame.transform.scale(bgd_image, (800, 600))
        if (pygame.key.get_pressed()[pygame.K_w]):

            bgd_image = pygame.image.load(os.path.join(
                "color changes", "Assets", "white_screen.jpg")).convert()
            bgd_image_scaled = pygame.transform.scale(bgd_image, (800, 600))
        draw_screen(xpos, ypos, bgd_image_scaled, sizex, sizey)


if __name__ == '__main__':
    main()
