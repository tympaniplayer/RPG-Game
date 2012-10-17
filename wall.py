# Wall Sprite
import pygame

# Define some colors
black = ( 0, 0, 0)
white = (255, 255, 255)
green = ( 0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y,width,height):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
