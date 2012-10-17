# Projectile Sprite
import pygame

# Define some colors
black = ( 0, 0, 0)
white = (255, 255, 255)
green = ( 0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
class Bullet(pygame.sprite.Sprite):
    #Attributes
    direction = "down"
    def __init__(self,x, y, initial_direction):
        pygame.sprite.Sprite.__init__(self)

        if initial_direction == "left" or initial_direction == "right":
            self.image = pygame.Surface([x, y])
        else:
            self.image = pygame.Surface([y,x])
        self.image.fill(blue)
        
        self.rect = self.image.get_rect()
        self.direction = initial_direction

    def update(self):
        if self.direction == "left":
            self.rect.x -= 10
        elif self.direction == "right":
            self.rect.x += 10
        elif self.direction == "up":
            self.rect.y -= 10
        else:
            self.rect.y += 10
