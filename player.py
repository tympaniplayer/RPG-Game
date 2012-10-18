# Player Sprite

import pygame

# Define some colors
black = ( 0, 0, 0)
white = (255, 255, 255)
green = ( 0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    # -- Attributes
    change_x = 0
    change_y = 0
    # Facing directions
    direction = "down"
    

    frame = 5

    # Constructor.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = []

        for i in range(1, 17):
            img = pygame.image.load("player"+str(i)+".png").convert()
            img.set_colorkey(white)
            self.images.append(img)

        self.image = self.images[1]

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100


    # Change the speed of the player
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y
          

    # Find a new position for the player
    def update(self,walls):
        # Get the old position, in case we need to go back to it
        old_x=self.rect.left
        new_x=old_x+self.change_x
        self.rect.left = new_x
         
        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.left=old_x
 
        old_y=self.rect.top
        new_y=old_y+self.change_y
        self.rect.top = new_y
         
        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.top=old_y

            
        # If we are moving left to right
        if self.change_x > 0:
            self.frame += 1
            self.direction = "right"

            if self.frame > (4 * 4) - 1:
                self.frame = 0

            self.image = self.images[self.frame//4+8]

        if self.change_x < 0:
            self.frame += 1
            self.direction = "left"
            
            if self.frame > (4 * 4) - 1:
                self.frame = 0
            self.image = self.images[self.frame//4+4]

        # If we are moving up and down
        if self.change_y > 0:
            self.frame +=1
            self.direction = "down"

            if self.frame > (4 * 4) - 1:
                self.frame = 0

            self.image = self.images[self.frame//4]

        if self.change_y < 0:
            self.frame += 1
            self.direction = "up"

            if self.frame > (4 * 4) - 1:
                self.frame = 0

            self.image = self.images[self.frame//4 + 12]
