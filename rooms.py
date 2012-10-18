import pygame
import wall


from wall import *
def TestRoom():
    wall_list = pygame.sprite.RenderPlain()

    walls = [[0,0,20,250],
             [0,350,20,250],
             [780,0,20,250],
             [780,350,20,250],
             [20,0,760,20],
             [20,580,760,20],
             [390,80,20,400]]

    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3])
        wall_list.add(wall)
    return wall_list
