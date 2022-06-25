from calendar import c
import os
import sys
import pygame
from pygame.locals import *

pygame.init()

position = [1000,600]
window  = pygame.display.set_mode(position)
pygame.display.set_caption("Collision")
mouse = pygame.image.load(os.path.join('collision','Assets','mouse.png'))
mouse_scaled = pygame.transform.scale(mouse,(150,75))
def main():
    x_pos ,y_pos = 0,510
    while True:
        window.fill((255,255,255))
        window.blit(mouse_scaled,(x_pos,y_pos))
        gola = pygame.draw.circle(window, (155, 205, 15), (500,550), 50) #draw a circle
        blocked = False
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
                pygame.quit()
                sys.exit()
        if (pygame.key.get_pressed()[pygame.K_LEFT]):
            x_pos -= 1
            if(x_pos < 0):
                x_pos = 0
        if (pygame.key.get_pressed()[pygame.K_RIGHT]):
            x_pos += 1
            print(x_pos)
            if(x_pos > 845):
                x_pos = 845
            if(x_pos >= 315):
                blocked = True
                x_pos = 315
                font = pygame.font.SysFont("comicsansms", 30)
                text = font.render("Blocked", True, (255, 0, 0))
                window.blit(text, (500, 500))
        pygame.display.flip()

if __name__ == "__main__":
    main()