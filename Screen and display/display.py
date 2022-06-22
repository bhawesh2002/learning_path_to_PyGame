import sys
import pygame  # for pygame.init()
from pygame.locals import *  # import the locals from the pygame module

pygame.init()  # initialize the pygame module

height = 800  # height of the screen
width = 600  # set the width of the screen
logo = pygame.image.load(
    "Screen and Display\logo\display.png")  # load the logo

# create a window of the specified size
# set the window size and create a resizeable window
window = pygame.display.set_mode((height, width), pygame.RESIZABLE)

# set the caption of the window
pygame.display.set_caption("Display Tweaks")
pygame.display.set_icon(logo)  # set the icon of the window


def draw_screen():
    gola = pygame.draw.circle(window, (155, 255, 255), (400, 300), 50)
    tricone = pygame.draw.polygon(window, (215, 110, 200), ((500, 300), (400, 400), (500, 400)))


def main():
    while(True):  # infinite game loop
        pygame.display.update()  # update the display
        for event in pygame.event.get():  # check for events
            if event.type == QUIT:  # if the user clicks the close button
                pygame.quit()  # quit the pygame module
                sys.exit()  # exit the program
            # if the user releases the 'f' key
            if (event.type == pygame.KEYUP and event.key == pygame.K_f):
                pygame.display.toggle_fullscreen()  # toggle fullscreen
        window.fill((65, 75, 90))  # fill the window with a color
        draw_screen()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
