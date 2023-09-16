# 1. Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2. Define Constansts
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3. Intialiaze World
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load Assets
ballImage = pygame.image.load('images/ball.png')
# 5. Initialize Variables
ballRect = ballImage.get_rect(center = (320, 240))
        
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height

ballRect.x = random.randrange(0, MAX_WIDTH)
ballRect.y = random.randrange(0, MAX_HEIGHT)

xSpeed = 5
ySpeed = 5



# 6. Loop Forever
while True:
    
    # 7. Check and handle events
    for event in pygame.event.get():
        # Close the program if close button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ballRect.move_ip(xSpeed, ySpeed)
    # 8. Do any "per frame" actions
    if ballRect.x <0 or ballRect.x > WINDOW_WIDTH:
        xSpeed = -xSpeed
    
    if ballRect.y <0 or ballRect.y > WINDOW_HEIGHT:
        ySpeed = -ySpeed
    
    # 9. Clear the window before drawing again
    window.fill(BLACK)
    
    # 10. Draw the window elements
    window.blit(ballImage, ballRect)
    
    # 11. Update the Window
    pygame.display.update()
    
    # 12. Slow Things Down
    clock.tick(FRAMES_PER_SECOND) #make pygame wait
