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
 
colors = [WHITE, RED, BLUE, GREY, ORANGE, GREEN, PINK, PURPLE, BROWN, CORAL, GOLD, IVORY, LAVENDER, LTBLUE, MINT, TURQUOISE]

clength = len(colors)


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




dx = random.randint(-10, 10)
dy = random.randint(-10, 10)

dx2 = random.randint(-10, 10)
dy2 = random.randint(-10, 10)

dx3 = random.randint(-10, 10)
dy3 = random.randint(-10, 10)

x = int(SCREEN_WIDTH/2)
y = int(SCREEN_HEIGHT/2)

x2 = int(SCREEN_WIDTH/2)
y2 = int(SCREEN_HEIGHT/2)

x3 = int(SCREEN_WIDTH/2)
y3 = int(SCREEN_HEIGHT/2)

rad = random.randint(10, 80)
rad2 = random.randint(10, 80)
rad3 = random.randint(10, 80)

ball_color = random.choice(colors)
ball_color2 = random.choice(colors)
ball_color3 = random.choice(colors)

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

    # This is outside because of variable scoping.


    pygame.draw.circle(screen, ball_color, [x, y], rad)
    pygame.draw.circle(screen, ball_color2, [x2, y2], rad2)
    pygame.draw.circle(screen, ball_color3, [x3, y3], rad3)


    if x > SCREEN_WIDTH or x < 0:
        dx = dx * -1
        ball_color = random.choice(colors)


    if y < 0 or y > SCREEN_HEIGHT:
        dy = dy * -1
        ball_color = random.choice(colors)
    
    
    if x2 > SCREEN_WIDTH or x2 < 0:
        dx2 = dx2 * -1
        ball_color2 = random.choice(colors)

    if y2 < 0 or y2 > SCREEN_HEIGHT:
        dy2 = dy2 * -1
        ball_color2 = random.choice(colors)
        
    if x3 > SCREEN_WIDTH or x3 < 0:
        dx3 = dx3 * -1
        ball_color2 = random.choice(colors)

    if y3 < 0 or y3 > SCREEN_HEIGHT:
        dy3 = dy3 * -1
        ball_color3 = random.choice(colors)

    x += dx
    y += dy
    
    x2 += dx2
    y2 += dy2
    
    x3 += dx3
    y3 += dy3
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
