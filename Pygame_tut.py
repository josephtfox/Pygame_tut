# Title: Pygame Tutorial 
# Author: Joseph Fox 
# Email: josephtfox@gmail.com

# Notes:
# - the position of (0,0) begins at the top left of the window
#

import pygame 
from sys import exit

# Starts pygame and iniates all of the parts of the pygame library
# Display Surface which is the window the game runs off of, parameters are the width and the height of the window 
# Add the tile to the window
# Initilaized the clock for the game
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# Creating the regular surface (Picture)
sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/Ground_pygame.p')



# The while true loop allows the game to run 
while True:

    # looping thought all of the events to get player input
    for event in pygame.event.get():

        # if the "X" button on  the window is pressed then it will quit pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            # Removes the while true loop to stop error
            exit()

    # BLIT (Block, Image, Transfer) =  putting one surface onto another surface (surface you want to place, Position)
    screen.blit(test_surface,(0,0))

    # Draw all our elements
    # Updates the display surface
    pygame.display.update()
    # Sets the Max framerate for the game
    clock.tick(60)