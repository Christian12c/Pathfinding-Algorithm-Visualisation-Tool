#Importing modules, procedures and constants that are referenced in this file
from random import choices
from random import randint
from random import randrange
from math import floor
import pygame
import sys
from pygame_Setup import SCREEN, BLACK, WHITE, PURPLE, BLOCK_SIZE, GRID_HEIGHT, GRID_WIDTH
from time import sleep

#Initialises all imported pygame modules
pygame.init()

grid = []
for i in range(GRID_HEIGHT):
    grid.append([])
    for j in range(GRID_WIDTH):
        grid[i].append([])

originalY1,originalX1,originalY2,originalX2 = 0,0,GRID_HEIGHT-1,GRID_WIDTH-1

#Divides the grid horizontally
def divideH(grid,y1,x1,y2,x2):
    pygame.event.get()
    #If the smallest subgrid is of width/height of 1
    if x2-x1<=1 or y2-y1<=1:
        return

    #Finds a y-coordinate that the wall can be drawn from
    wallYPosition = -1
    while wallYPosition == -1:
        wallYPosition = choices([2*i+1 for i in range(floor(y1/2), floor(y2/2))])[0]
        if x1 == originalX1 and x2 == originalX2:
            if " " in grid[wallYPosition][x1:x2+2]:
                wallYPosition = -1
        elif x1 != originalX1 and x2 == originalX2:
            if " " in grid[wallYPosition][x1-1:x2+2]:
                wallYPosition = -1
        elif x1 == originalX1 and x2 != originalX2:
            if " " in grid[wallYPosition][x1:x2+3]:
                wallYPosition = -1
        elif x1 != originalX1 and x2 != originalX2:
            if " " in grid[wallYPosition][x1-1:x2+3]:
                wallYPosition = -1

    #Adds the "blocks" to make the wall
    for i in range(x1,x2+1):                    
        grid[wallYPosition][i] = "•"
        pygame.draw.rect(SCREEN, PURPLE, (BLOCK_SIZE*i + 1.5, BLOCK_SIZE*wallYPosition + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
        pygame.display.flip()
    sleep(0.03)

    #Finds an x-coordinate that can be a gap
    wallXGap = -1
    while wallXGap == -1:
        wallXGap = choices([2*i for i in range(floor(x1/2), floor((x2+1)/2))])[0]
    grid[wallYPosition][wallXGap] = " "
    pygame.draw.rect(SCREEN, WHITE, (BLOCK_SIZE*wallXGap + 1.5, BLOCK_SIZE*wallYPosition + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
    pygame.display.flip()

    #Recursion for the top subGrid
    height = (wallYPosition-1)-y1
    width = x2-x1
    if width > height:
        divideV(grid,y1,x1,wallYPosition-1,x2)
    elif width < height:
        divideH(grid,y1,x1,wallYPosition-1,x2)
    else:
        x = randint(0,1)
        if x == 0:
            divideV(grid,y1,x1,wallYPosition-1,x2)
        else:
            divideH(grid,y1,x1,wallYPosition-1,x2)
            
    #Recursion for the bottom subGrid
    height = y2-(wallYPosition+1)
    width = x2-x1
    if width > height:
        divideV(grid,wallYPosition+1,x1,y2,x2)
    elif width < height:
        divideH(grid,wallYPosition+1,x1,y2,x2)
    else:
        x = randint(0,1)
        if x == 0:
            divideV(grid,wallYPosition+1,x1,y2,x2)
        else:
            divideH(grid,wallYPosition+1,x1,y2,x2)


#Divides the grid horizontally
def divideV(grid,y1,x1,y2,x2):
    pygame.event.get()
    #If the smallest subgrid is of width/height of 1
    if x2-x1<=1 or y2-y1<=1:
        return

    #Finds an x-coordinate that the wall can be drawn from
    wallXPosition = -1
    while wallXPosition == -1:
        wallXPosition = choices([2*i+1 for i in range(floor(x1/2), floor(x2/2))])[0]
        if y1 == originalX1 and y2 == originalY2:
            if " " in [grid[i][wallXPosition] for i in range(y1,y2+1)]:
                wallYPosition = -1
        elif y1 != originalX1 and y2 == originalY2:
            if " " in [grid[i][wallXPosition] for i in range(y1-1,y2+1)]:
                wallYPosition = -1
        elif y1 == originalX1 and y2 != originalY2:
            if " " in [grid[i][wallXPosition] for i in range(y1,y2+2)]:
                wallYPosition = -1
        elif y1 != originalX1 and y2 != originalY2:
            if " " in [grid[i][wallXPosition] for i in range(y1-1,y2+2)]:
                wallXPosition = -1

    #Adds the "blocks" to make the wall
    for i in range(y1,y2+1):
        grid[i][wallXPosition] = "•"
        pygame.draw.rect(SCREEN, PURPLE, (BLOCK_SIZE*wallXPosition + 1.5, BLOCK_SIZE*i + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
        pygame.display.flip()
    sleep(0.03)

    #Finds a y-coordinate that can be a gap
    wallYGap = -1
    while wallYGap == -1:
        wallYGap = choices([2*i for i in range(floor(y1/2), floor((y2+1)/2))])[0]
    grid[wallYGap][wallXPosition] = " "
    pygame.draw.rect(SCREEN, WHITE, (BLOCK_SIZE*wallXPosition + 1.5, BLOCK_SIZE*wallYGap + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
    pygame.display.flip()

    #Recursion for the left subGrid
    height = y2-y1
    width = (wallXPosition-1)-x1
    if width > height:
         divideV(grid,y1,x1,y2,wallXPosition-1)
    elif width < height:
        divideH(grid,y1,x1,y2,wallXPosition-1)
    else:
        x = randint(0,1)
        if x == 0:
            divideV(grid,y1,x1,y2,wallXPosition-1)
        else:
            divideH(grid,y1,x1,y2,wallXPosition-1)

    #Recursion for the right subGrid
    height = y2-y1
    width = x2-(wallXPosition+1)
    if width > height:
        divideV(grid,y1,wallXPosition+1,y2,x2)
    elif width < height:
        divideH(grid,y1,wallXPosition+1,y2,x2)
    else:
        x = randint(0,1)
        if x == 0:
            divideV(grid,y1,wallXPosition+1,y2,x2)
        else:
            divideH(grid,y1,wallXPosition+1,y2,x2)
