# Basic Pygame Structure

import pygame                               # Imports pygame and other libraries

# Define Classes (sprites) here

pygame.init()                               # Pygame is initialised (starts running)

screen = pygame.display.set_mode([700,500]) # Set the width and height of the screen [width,height]
pygame.display.set_caption("Hugh-Nelson.game")       # Name your window
done = False                                # Loop until the user clicks the close button.
clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
black    = (0, 0, 0)                 # Define some colors using rgb values.  These can be
white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.
speed = 10
rect_x, rect_y = 40,40
# Define additional Functions and Procedures here

# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():        # Check for an event (mouse click, key press)
        if event.type == pygame.QUIT:       # If user clicked close window
            done = True                     # Flag that we are done so we exit this loop

    # Update sprites here
    rect_x += 1
    rect_y -= 2
    screen.fill(black)

    pygame.draw.rect(screen, white, pygame.Rect(rect_x, rect_y, 100, 160))

    pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
    clock.tick(20)                          # Limit to 20 frames per second


pygame.quit()                               # Close the window and quit.

