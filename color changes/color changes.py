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


def draw_screen():
    window.fill((255, 255, 255))
    beach_ball_resized = pygame.transform.scale(beach_ball, (150, 150))
    window.blit(beach_ball_resized,(200,200))


def main():
    while(True):
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()
        draw_screen()


if __name__ == '__main__':
    main()
