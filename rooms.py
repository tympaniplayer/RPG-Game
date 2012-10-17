# This file will contain room definitions
# unaccaptble room names are things like room1() room2() etc.
# use your best judgement on what to call a room.

import pygame
import walls

from walls import *

def playerHouse():
	wall_list = pygame.sprite.RenderPlain()
	# List of walls here
	walls = [[0,0,20,250],
                [0,350,20,250],
                [780,0,20,250],
                [780,350,20,250],
                [20,0,760,20],
                [20,580,760,20],
                [390,50,20,500]
                ]
	for item in walls:
            wall = Wall(item[0], item[1]. item[2], item[3], item[4])
            wall_list.add(wall)
        return wall_list
