import sys  # for sys.exit()
import os
from xml.dom.minidom import DOMImplementation  # for os.path.join()
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
    window.fill((0, 0, 0))  # fill the window with black
    # draw the ball on the 1.window of 2.light green color 3.position 4.radius
    ball = pygame.draw.circle(window, (22, 255, 22), (x_pos, y_pos), 25)
    pygame.display.update()  # update the display
    for event in pygame.event.get():  # get all the events
        # if the event is a quit event or a keydown event with the q key
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()  # quit the game
            sys.exit()  # exit the game
    if(pygame.key.get_pressed()[K_RIGHT]):  # if the right key is pressed
        # if the ball is not at the right edge of the screen
        if(x_pos < dimensions.topright[0]):
            x_pos += 1  # move the ball to the right
        elif(x_pos == dimensions.topright[0]):
            while(x_pos != dimensions.centerx):
                x_pos -= 1
                window.fill((0, 0, 0))
                ball = pygame.draw.circle(window, (22, 255, 22), (x_pos, y_pos), 25)
                pygame.display.update()
    if(pygame.key.get_pressed()[K_LEFT]):
        if(x_pos > dimensions.topleft[0]):
            x_pos -= 1
        elif(x_pos == dimensions.topleft[0]):
            while(x_pos != dimensions.centerx):
                x_pos += 1
                window.fill((0,0,0))
                ball = pygame.draw.circle(window, (22, 255, 22), (x_pos, y_pos), 25)
                pygame.display.update()
    if(pygame.key.get_pressed()[K_DOWN]):
        if(y_pos < dimensions.bottomleft[1]):
            y_pos += 1
        else:
            y_pos = dimensions.bottomleft[1]
    if(pygame.key.get_pressed()[K_UP]):
        if(y_pos > dimensions.topleft[1]):
            y_pos -= 1
        else:
            y_pos = dimensions.topleft[1]
