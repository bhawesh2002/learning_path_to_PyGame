from asyncio.windows_events import NULL
import pygame  # imports the pygame library as module into the program

pygame.init()  # function call attempts  to initialise all the pygame  modules
height = 800
width = 600

# creates a window of the specified size
window = pygame.display.set_mode((height, width))

while(pygame.get_init() == True):  # keep showing the screen until the user closes it
    NULL  # do nothing

pygame.quit()  # quit all the initialized modules when python finishes running
