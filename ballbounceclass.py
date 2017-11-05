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
 



pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [WHITE, RED, BLUE, GREY, ORANGE, GREEN, PINK, PURPLE, BROWN, CORAL, GOLD, IVORY, LAVENDER, LTBLUE, MINT, TURQUOISE]


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x, y, dx, dy, rad):  
    # Attributes of the bouncing ball 
        self.x = x
        self.y = y  
        self.dx = dx
        self.dy = dy 
        self.rad = rad 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(colors) # This is outside because of variable scoping.

        if self.x >= screen_width - self.rad or self.x < self.rad:
            self.dx = self.dx * -1

        if self.y >= screen_height - self.rad or self.y < self.rad:
            self.dy = self.dy * -1

        self.x += self.dx
        self.y += self.dy

        pygame.draw.circle(screen, ball_color, [self.x, self.y], self.rad)

balls = []
rx = int(SCREEN_WIDTH/2)
ry = int(SCREEN_HEIGHT/2)

num = int(input("How many balls?: "))

for each in range(num):
	rdx = random.randint(-10, 10)
	rdy = random.randint(-10, 10)
	rrad = random.randint(10, 80)
	ball = BouncingBall(rx, ry, rdx, rdy, rrad)
	balls.append(ball)

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
    for item in balls:
    	item.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


