import sys
import pygame
from pygame.locals import *

pygame.init()

width,height = 800*600
window = pygame.display.set_mode((width,height))
dimensions = window.get_rect()