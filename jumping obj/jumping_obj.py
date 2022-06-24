import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height = 600
width = 800

window = pygame.display.set_mode((width,height), pygame.RESIZABLE)
soccer_ball = pygame.image.load(os.path.join('jumping obj','Assets','soccer-ball.jpg')).convert()
soccer_ball_scaled = pygame.transform.scale(soccer_ball, (150,150))
soccer_ball_scaled.set_colorkey((255,255,255))
while(True):
    window.fill((255,255,255))  # fill the screen with a light green color
    window.blit(soccer_ball_scaled, (100,100))
    pygame.display.update()
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()