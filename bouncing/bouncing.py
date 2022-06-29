from cmath import e
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
    resist = 50
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
                while(y_pos >= (dimensions.centery + resist)):
                    window.fill((0, 0, 0))
                    ball = pygame.draw.circle(
                        window, (22, 255, 22), (x_pos, y_pos), 25)
                    pygame.display.update()
                    if(pygame.key.get_pressed()[K_RIGHT]):
                        if(x_pos <= dimensions.topright[0] - 25):
                            x_pos += 0.1
                        else:
                            x_pos = dimensions.topright[0] - 25
                    if(pygame.key.get_pressed()[K_LEFT]):
                        if(x_pos >= dimensions.topleft[0] + 25):
                            x_pos -= 0.1
                        else:
                            x_pos = dimensions.topleft[0] + 25
                    y_pos -= 0.1
                    resist += 0.1
        pygame.display.update()


if __name__ == "__main__":
    main()
