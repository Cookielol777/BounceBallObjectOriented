# 1. 
# a. Import packages
import pygame
from pygame.locals import *
import random

# b. Create Ball Class
class Ball():
# c. Instantiate Ball Class
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window #remember window so we can draw later
        self.windowWidth = 640
        self.windowHeight = 480
        self.image = pygame.image.load('images/ball.png')
# 2. Getting rect of image, determining min and max values for width and height (defined by x, y, width, height)
        self.ballRect = self.image.get_rect(center = (320, 240))
        
        
        maxWidth = windowWidth - self.ballRect.width
        maxHeight = windowHeight - self.ballRect.height
        
# 3. Pick random start position
        self.ballRect.x = random.randrange(0, self.windowWidth)
        self.ballRect.y = random.randrange(0, self.windowHeight)
        
# 4. Pick random speed between -4 and 4, but not zero in x and y direction
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

# 5. Define update method
    def update(self):
        # Check for hitting wall, if so change that direction
        if self.ballRect.x <0 or self.ballRect.x > self.windowWidth:
                 self.xSpeed = - self.xSpeed
        if self.ballRect.y <0 or self.ballRect.y > self.windowHeight:
                self.ySpeed = -self.ySpeed
    
        # Update the Ball's x and y, using the speed in two directions
        self.ballRect.move_ip(self.xSpeed, self.ySpeed)

# 6. Define draw method     
    def draw(self):
            self.window.blit(self.image, self.ballRect)