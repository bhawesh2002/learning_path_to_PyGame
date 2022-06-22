import sys  # impoirt sys module for system calls
import pygame  # imports the pygame library as module into the program
from pygame.locals import *  # imports the pygame.locals module to get the QUIT event

pygame.init()  # function call attempts  to initialise all the pygame  modules
height = 800  # sets the height of the screen
width = 600  # sets the width of the screen

# creates a window of the specified size
window = pygame.display.set_mode((height, width))

while(True):   # infinite loop
    pygame.display.update()  # updates the display
    for event in pygame.event.get():  # gets all the events from the event queue
        if event.type == QUIT:  # if the event is a quit event
            pygame.quit()  # quits the game
            sys.exit()  # exits the program

# Modules that are initialized also usually have a quit() function that will clean up.
# There is no need to explicitly call these,
# as pygame will cleanly quit all the initialized modules when python finishes.
