import pygame  # imports the pygame library as module into the program

pygame.init()  # function call attempts  to initialise all the pygame  modules
height = 800
width = 600

# creates a window of the specified size
window = pygame.display.set_mode((height, width))

# Modules that are initialized also usually have a quit() function that will clean up.
# There is no need to explicitly call these,
# as pygame will cleanly quit all the initialized modules when python finishes.
