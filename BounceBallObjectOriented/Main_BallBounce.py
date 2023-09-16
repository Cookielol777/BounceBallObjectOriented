# 1. Packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *

def main():
    # 2. Constants
    BLACK = (0, 0, 0)
    windowWidth = 640
    windowHeight = 480
    FRAMES_PER_SECOND = 30
     # 3. Initialize World
    pygame.init()
    window = pygame.display.set_mode((windowWidth, windowHeight))
    clock = pygame.time.Clock()
    
    # 4. Load Assets
    ballImage = pygame.image.load('images/ball.png')
    
    # 5. Initialize variables
    oBall = Ball(window, windowWidth, windowHeight)
    
    # 6. Loop Forever
    while True:
    # 7. Check and handle events
     for event in pygame.event.get():
        # Close the program if close button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8. Do any per-frame actions
        oBall.update()
    
    # 9. Clear window before drawing again
        window.fill(BLACK)
    
    #10. Draw window elements
        oBall.draw()
        
    # 11. Update window
        pygame.display.update()

    # 12. Slow Down
        clock.tick(FRAMES_PER_SECOND) #make pygame wait
# check if this is the module from the command line
if (__name__ == '__main__'):
    main()