import sys  # for sys.exit()
import os  # for os.path.join()
import pygame  # import the pygame module
# import the pygame.locals for easier access to key presses and mouse positions
from pygame.locals import *

pygame.init()  # initialize the pygame module

width, height = 800, 600  # set the width and height of the screen

window = pygame.display.set_mode((width, height))  # create the window
dimensions = window.get_rect()  # get the dimensions of the window
x_pos = 400  # set the x position of the ball
y_pos = 0  # set the y position of the ball
while True:  # loop forever
    window.fill((0, 0, 0))  # fill the window with white
    # draw the ball on the 1.window of 2.light green color 3.position 4.radius
    ball = pygame.draw.circle(window, (22, 255, 22), (x_pos, y_pos), 25)
    pygame.display.update()  # update the display
    for event in pygame.event.get():  # get all the events
        # if the event is a quit event or a keydown event with the q key
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()  # quit the game
            sys.exit()  # exit the game
    if(pygame.key.get_pressed()[K_RIGHT]):  # if the right key is pressed
        if(x_pos < dimensions.topright[0]):  # if the ball is not at the right edge of the screen
            x_pos += 1  # move the ball to the right
        else:  # if the ball is at the right edge of the screen
            x_pos = dimensions.width  # set the ball to the right edge of the screen