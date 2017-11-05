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

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


# Your SnowFlake class
class Snowflake():
	def __init__(self, x, y, dy, rad):
		self.x = x
		self.y = y
		self.dy = dy
		self.rad = rad
		
	def fall(self, screen, color, width, height):
		color = WHITE
		self.y += self.dy
		pygame.draw.circle(screen, color, [self.x, self.y], self.rad)


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 3

# Snow List
snow_list = []

for each in range(random.randint(20,50)):
	rdy = random.randint(1, 10)
	rrad = random.randint(20, 40)
	rx = int(randint(0,700))
ry = int(randint(0,500))
	snow1 = Snowflake(rx, ry, rdy, rrad)
	snow_list.append(snow1)
	
	
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
    # Begin Snow
    for item in snow_list:
    	item.fall(screen, WHITE, 700, 500)
		
    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
