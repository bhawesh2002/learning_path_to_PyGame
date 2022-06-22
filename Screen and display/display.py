from re import T
import sys  # for sys.exit()
import pygame  # for pygame.init()
from pygame.locals import *  # import the locals from the pygame module

pygame.init()  # initialize the pygame module

height = 800  # height of the screen
width = 600  # set the width of the screen
logo = pygame.image.load(
    "Screen and Display\logo\display.png")  # load the logo
# create a window of the specified size
window = pygame.display.set_mode((height, width), pygame.RESIZABLE) # set the window size and create a resizeable window
pygame.display.set_caption("Display Tweaks")  # set the caption of the window
pygame.display.set_icon(logo)  # set the icon of the window

while(True):  # infinite game loop
    pygame.display.update()  # update the display
    for event in pygame.event.get():  # check for events
        if event.type == QUIT:  # if the user clicks the close button
            pygame.quit()  # quit the pygame module
            sys.exit()  # exit the program
        if (event.type == pygame.KEYUP and event.key == pygame.K_f):  # if the user releases the 'f' key
            pygame.display.toggle_fullscreen()  # toggle fullscreen
    window.fill((65,75,90))  # fill the window with a color
