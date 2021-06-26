#Importing modules, procedures and constants that are referenced in this file
import pygame
import sys

pygame.init()
SCREEN_WIDTH = 1255
SCREEN_HEIGHT = 570
BLOCK_SIZE = 25
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (211,211,211)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (153,50,204)
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
SCREEN.fill(BLACK)

GRID_WIDTH = 50
GRID_HEIGHT = 20

def createVisualGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #' ' represents an empty space
            if grid[i][j] == ' ' or grid[i][j] == []:
                pygame.draw.rect(SCREEN, WHITE, (BLOCK_SIZE*j + 1.5, BLOCK_SIZE*i + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
            #'•' represents a wall
            elif grid[i][j] == '•':
                pygame.draw.rect(SCREEN, PURPLE, (BLOCK_SIZE*j + 1.5, BLOCK_SIZE*i + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
            #'*' represents a start/end node
            elif grid[i][j] == '*':
                pygame.draw.rect(SCREEN, BLUE, (BLOCK_SIZE*j + 1.5, BLOCK_SIZE*i + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
            #'_' represents a node in the search space
            elif grid[i][j] == '_':
                pygame.draw.rect(SCREEN, GREEN, (BLOCK_SIZE*j + 1.5, BLOCK_SIZE*i + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
            #'o' represents a node in the path
            elif grid[i][j] == 'o':
                pygame.draw.rect(SCREEN, GREEN, (BLOCK_SIZE*j + 1.5, BLOCK_SIZE*i + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
                pygame.draw.rect(SCREEN, BLUE, (BLOCK_SIZE*j + 4.5, BLOCK_SIZE*i + 73, BLOCK_SIZE - 10, BLOCK_SIZE - 10))
