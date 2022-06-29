import sys
import pygame
from pygame.locals import *

pygame.init()

width, height = 800, 600

window = pygame.display.set_mode((width, height))
dimensions = window.get_rect()
gravity = 0.5


def main():
    x_pos = dimensions.centerx
    y_pos = dimensions.centery
    counter = 3
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()
        if(y_pos <= dimensions.bottomright[1] - 25):
            y_pos += gravity
            window.fill((0, 0, 0))
            ball = pygame.draw.circle(
                window, (22, 255, 22), (x_pos, y_pos), 25)
            pygame.display.update()
            if(y_pos >= dimensions.bottomright[1] - 25):
                counter -= 1
                print(counter)
        pygame.display.update()


if __name__ == "__main__":
    main()
