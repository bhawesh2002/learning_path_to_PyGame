import sys   # for sys.exit()
import pygame #import pygame module

from pygame.locals import *  #import contains of pygame.locals

pygame.init() #initialize pygame

height = 800 #height of the window
width = 600 #width of the window 

window = pygame.display.set_mode((height, width), pygame.RESIZABLE) #create a window
font = pygame.font.SysFont("comicsansms", 30) #create a font object
text = font.render("Hello World", True, (0, 0, 0)) #create a text object that will be displayed on the screen

def draw_screen(): #function to draw the screen
    window.fill((255, 255, 255)) #fill the screen with white color
    window.blit(text, (300, 400)) #blit the text object to the screen
    pygame.display.update() #update the screen


def main(): #main function
    while(True):
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()
        draw_screen() #call the draw_screen function


if __name__ == "__main__":
    main()
