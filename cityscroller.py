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
WHITE = (255, 250, 250)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]
bg = pygame.image.load("night.jpg")
car= pygame.image.load("car2.jpg")
cpos = car.get_rect()

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x_point, y_point, width, height, color):
    	self.x_point = x_point
    	self.y_point = y_point
    	self.width = width
    	self.height = height
    	self.color = color
    def draw(self):
    	pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height))

    def move(self, speed):
    	self.x_point += (-speed)

class Scroller(object):

    def __init__(self, width, height, color, speed, maxh):
    	self.width = width
    	self.height = height
    	self.color = color
    	self.speed = speed
    	self.buildings = []
    	self.maxh = maxh

    def add_buildings(self):
        current_width = 0
        while current_width <= self.width:
        	self.add_building(current_width)
        	current_width += self.buildings[-1].width
        

    def add_building(self, x_location):
        building_width = random.randint((self.width // 20), (self.width // 4))
        
        building_height = random.randint(0, self.maxh)
        
        y_location = self.height - building_height
        
        self.buildings.append(Building(x_location, y_location, building_width, building_height, self.color))

    def draw_buildings(self):
        for i in self.buildings:
        	i.draw()

    def move_buildings(self):
        for j in self.buildings:
        	j.move(self.speed)
        self.add_building((self.buildings[-1].x_point)+(self.buildings[-1].width))

class Snowflake:
	def __init__(self, x, y, speed, rad):
		self.x = x
		self.y = y
		self.speed = speed
		self.rad = rad
	
	def fall(self, screen, color, width, height):
		
		color = WHITE
		self.speed = random.randint(1,2)
		self.y += self.speed
		pygame.draw.circle(screen, WHITE, [self.x, self.y], self.rad)
		
		if self.y > 600:
			self.y = random.randint(-40,-10)
			self.x = random.randint(0, 750) 
        


FRONT_SCROLLER_COLOR = (17, 9, 89)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (0,0,30)

front_scroller = Scroller(SCREEN_WIDTH, 650, FRONT_SCROLLER_COLOR, 3, 300)
middle_scroller = Scroller(SCREEN_WIDTH, 650, MIDDLE_SCROLLER_COLOR, 2, 500)
back_scroller = Scroller(SCREEN_WIDTH, 650, BACK_SCROLLER_COLOR, 1, 650)

front_scroller.add_buildings()
middle_scroller.add_buildings()
back_scroller.add_buildings()

speed = 3
snow_list = []

for i in range(random.randint(400,700)):
	x = random.randint(0,800)
	y = random.randint(0, 600)
	rad = random.randint(2,4)
	snow1 = Snowflake(x, y, speed, rad)
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
    screen.blit(bg, (0,0))
    

    # --- Drawing code should go here
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    for j in snow_list:
    	j.fall(screen, WHITE, 800, 600)
    screen.blit(car, cpos)
    cpos = cpos.move(1,0)
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
