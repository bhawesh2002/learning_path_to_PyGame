import sys  
import pygame

from pygame.locals import *

pygame.init()

height = 800
width = 600

window = pygame.display.set_mode((height, width), pygame.RESIZABLE)
font = pygame.font.SysFont("comicsansms", 30)
text = font.render("Hello World", True, (0, 0, 0))

def draw_screen():
    window.fill((255, 255, 255))
    window.blit(text, (300, 400))
    pygame.display.update()


def main():
    while(True):
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()
        draw_screen()


if __name__ == "__main__":
    main()
