import sys
import pygame

from pygame.locals import *

pygame.init()

height = 800
width = 600

window = pygame.display.set_mode((height, width), pygame.RESIZABLE)

def main():
    window.fill((255, 255, 255))