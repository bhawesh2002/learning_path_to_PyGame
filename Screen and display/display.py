import sys # for sys.exit()
import pygame # for pygame.init()
from pygame.locals import * #import the locals from the pygame module

pygame.init()  #initialize the pygame module

height = 800 #height of the screen
width = 600 #set the width of the screen

pygame.display.set_mode((height,width))
pygame.display.set_caption("Display Tweaks")

while(True): #infinite game loop
    pygame.display.update() #update the display
    for event in pygame.event.get(): #check for events
        if event.type == QUIT: #if the user clicks the close button
            pygame.quit() # quit the pygame module
            sys.exit() # exit the program