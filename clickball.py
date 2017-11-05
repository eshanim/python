"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
ORANGE = (255,165,0)
PINK= (255,192,203)
PURPLE = (160, 32, 140)
BROWN = (165, 42, 42)
CORAL = (255, 127, 80)
GOLD = (255, 215, 0)
IVORY = (255, 255, 240)
LAVENDER = (230, 230, 250)
LTBLUE = (173, 216, 230)
MINT = (245, 255, 250)
TURQUOISE = (64, 224, 208)
 
colors = [BLACK, WHITE, RED, BLUE, GREY, ORANGE, GREEN, PINK, PURPLE, BROWN, CORAL, GOLD, IVORY, LAVENDER, LTBLUE, MINT, TURQUOISE]

clength = len(colors)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
x = 350
y = 250

dx = random.randint(-10,10)
dy = random.randint(-10,10)

rad = random.randint(20, 80)
index = random.randint(0, clength - 1)
col = colors[index]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True



	# --- Game logic should go here

	
	# --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(BLACK)

    # --- Drawing code should go here
	mpos = pygame.mouse.get_pos()
	pygame.draw.circle(screen, col, mpos, rad)
	x += dx
	y += dy
	
	if x > SCREEN_WIDTH or x < 0:
		dx = dx * -1
		index = random.randint(0, clength - 1)
		col = colors[index]
	if y < 0 or y > SCREEN_HEIGHT:
		dy = dy * -1
		index = random.randint(0, clength - 1)
		col = colors[index]


    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
