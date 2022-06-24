import sys
import os
import pygame
from pygame.locals import *

pygame.init()

height = 600
width = 1000
clock = pygame.time.Clock()
window = pygame.display.set_mode((width, height))
soccer_ball = pygame.image.load(os.path.join(
    'jumping obj', 'Assets', 'soccer-ball.png')).convert()
soccer_ball_scaled = pygame.transform.scale(soccer_ball, (110, 110))
soccer_ball_rect = soccer_ball_scaled.get_rect()
soccer_ball_scaled.set_colorkey((255,255,255))
x_dir = soccer_ball_rect.x
y_dir = soccer_ball_rect.y
background = pygame.image.load(os.path.join('jumping obj', 'Assets', 'background.jpg'))
background_scaled = pygame.transform.scale(background, (width, height))
def draw_screen():
    window.fill((255, 255, 255))  # fill the screen with a light green color
    window.blit(background_scaled, (0,0))
    window.blit(soccer_ball_scaled, (x_dir, y_dir))
    pygame.display.update()
    pygame.display.flip()


while(True):
    clock.tick(60)
    for event in pygame.event.get():
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_q)):
            pygame.quit()
            sys.exit()
    if(pygame.key.get_pressed()[pygame.K_RIGHT]):
        x_dir += 5
        if(x_dir > 850):
            x_dir = 850
    if (pygame.key.get_pressed()[pygame.K_LEFT]):
        x_dir -= 5
        if(x_dir < 0):
            x_dir = 0
    if(pygame.key.get_pressed()[pygame.K_UP]):
        y_dir -= 5
        if(y_dir < 0):
            y_dir = 0
    if(y_dir < height - 150):
        y_dir += 3
        if(y_dir < height/2):
            y_dir += 1
    draw_screen()
