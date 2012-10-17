import pygame
import player
import wall
import bullet
import rooms
from player import *
from wall import *
from bullet import *
from rooms import *





        
        
        
screen_height = 700
screen_width = 1080
pygame.init()

# Set screen width and hight
size=[screen_width,screen_height]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

all_sprites_list = pygame.sprite.RenderPlain()

# Player
player = Player()
all_sprites_list.add(player)

wall_list = playerHouse()

# Edges
wall = Wall(0, 0, 0 , 700)
wall_list.add(wall)
wall = Wall(0,0, 1080, 0)
wall_list.add(wall)
wall = Wall(1080,0, 0, 700)
wall_list.add(wall)
wall = Wall(0, 700, 1080, 0)
wall_list.add(wall)


# Bullet
bullet_list = pygame.sprite.RenderPlain()

# Loop until the user clicks the close button.
done=False

# bool for edge detection of bullet

shot = False;

# speed multiplier for running
speedFactor = 1

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# Main Program Loop ---------------------------
while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit the loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3 * speedFactor,0)
            if event.key == pygame.K_d:
                player.changespeed(3 * speedFactor,0)
            if event.key == pygame.K_w:
                player.changespeed(0,-3 * speedFactor)
            if event.key == pygame.K_s:
                player.changespeed(0, 3 * speedFactor)
                
            if event.key == pygame.K_RCTRL and shot == False:
                bullet = Bullet(10, 2, player.direction)
                bullet.rect.x = player.rect.x + 10
                bullet.rect.y = player.rect.y + 15
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                shot = True
                  
        # Reset speed when key goes up      
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed((3 * speedFactor),0)
            if event.key == pygame.K_d:
                player.changespeed((-3 * speedFactor),0)
            if event.key == pygame.K_w:
                player.changespeed(0,(3 * speedFactor))
            if event.key == pygame.K_s:
                player.changespeed(0,(-3 * speedFactor))
            if event.key == pygame.K_RCTRL:
                shot = False

                
    # ALL EVENT PROCESSING SHOLD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
    player.update(wall_list)
    
    for bullet in bullet_list:
        bullet.update()

        wall_hit_list = pygame.sprite.spritecollide(bullet, wall_list, False)
        
        for wall in wall_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        if bullet.rect.y < -10 or bullet.rect.x > 1080:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased when the screen is cleared.
    screen.fill(white)

    all_sprites_list.draw(screen)
    wall_list.draw(screen)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    #Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(30)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE>
pygame.quit()
