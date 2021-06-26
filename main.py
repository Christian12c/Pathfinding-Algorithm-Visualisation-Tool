#Importing modules, procedures and constants that are referenced in this file
import pygame
from dropdown import Dropdown
from menu import Menu
import pygame_Setup
from dijkstraVisualised import Dijkstra
from aStarVisualised import AStar
from breadthFirstVisualised import BreadthFirst
from recursiveDivisionVisualised import divideH, divideV
from node import Node, AStarNode
from time import sleep

#A function that creates an empty grid of size 20x50 (height by width)
def createGrid():
    grid = []
    for i in range(20):
        grid.append([])
        for j in range(50):
            grid[i].append([])
    return grid
grid = createGrid()
graph = createGrid()

numberOfPoints = 0
startCoordinates = None
endCoordinates = None
recursiveDivision = False
algorithmChoice = None
solved = False
wallsPlacable = True

arrayOfMenuText = ["Recursive Division Maze", "Clear Board", "Clear Paths", "Visualise",]
menuWidth = len(arrayOfMenuText) + 1
menuHeight = 50

#Creates a dropdown
dropdown = Dropdown((0,0,pygame_Setup.SCREEN_WIDTH/menuWidth,menuHeight), (211,211,211), "Algorithms", pygame_Setup.SCREEN)
dropdown.addButton("Dijkstra's")
dropdown.addButton("A* Search")
dropdown.addButton("Breadth First Search")
dropdown.drawDropdown(fullList=False)

#Creates a menu
menu = Menu((pygame_Setup.SCREEN_WIDTH/menuWidth,0,pygame_Setup.SCREEN_WIDTH/menuWidth,menuHeight), (211,211,211), "Recursive Division Maze", pygame_Setup.SCREEN, menuWidth, menuHeight)
menu.addButton("Clear Board")
menu.addButton("Clear Path")
menu.addButton("Visualise")
menu.drawMenu()

#Draws the grid for the first time
pygame_Setup.createVisualGrid(grid)
while True:
    x, y = pygame.mouse.get_pos()
    #Menu update
    if y <= menuHeight or y <= menuHeight*4 and dropdown.getIsDropdownDown() == True:
        if x < pygame_Setup.SCREEN_WIDTH/menuWidth:
            dropdown.update(grid)
            algorithmChoice = dropdown.returnMain()
            if startCoordinates != None:
                grid[startCoordinates[0]][startCoordinates[1]] = '*'
            if endCoordinates != None:
                grid[endCoordinates[0]][endCoordinates[1]] = '*'
                
        else:
            menuIndex = menu.returnMenuItemIndex()
            #Recursive division menu option
            if menuIndex == 1 and dropdown.getIsDropdownDown() == False:
                numberOfPoints = 0
                startCoordinates = None
                endCoordinates = None
                wallsPlacable = False
                grid = createGrid()
                pygame_Setup.createVisualGrid(grid)
                solved = False
                divideH(grid,0,0,20 - 1,50 - 1)
                recursiveDivision = True
                
            #Clear board menu option
            elif menuIndex == 2 and dropdown.getIsDropdownDown() == False:
                numberOfPoints = 0
                startCoordinates = None
                endCoordinates = None
                recursiveDivision = False
                wallsPlacable = True
                grid = createGrid()
                pygame_Setup.createVisualGrid(grid)
                solved = False                
                
            #Clear Paths menu option
            elif menuIndex == 3 and dropdown.getIsDropdownDown() == False:
                wallsPlacable = True
                solved = False
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j] == 'o':
                            grid[i][j] = '_'
                if startCoordinates != None:
                    grid[startCoordinates[0]][startCoordinates[1]] = '*'
                if endCoordinates != None:
                    grid[endCoordinates[0]][endCoordinates[1]] = '*'
                pygame_Setup.createVisualGrid(grid)
                pygame.display.flip()

            #Visualise menu option
            elif menuIndex == 4:
                if algorithmChoice != "Algorithms" and startCoordinates != None and endCoordinates != None and dropdown.getIsDropdownDown() == False:
                    pygame.event.get()
                    if not solved:
                        #Dijkstra's algorithm
                        if algorithmChoice == "Dijkstra's":
                            a, path, spaceSearch = Dijkstra(grid, Node(startCoordinates), Node(endCoordinates))
                            #Shows the search space by adding it to the grid
                            for node in spaceSearch:
                                grid[node.get_position()[0]][node.get_position()[1]] = '_'
                                pygame.display.flip()
                            #Shows the path by adding it to the gri
                            for node in path:
                                grid[node[0]][node[1]] = 'o'
                                pygame.draw.rect(pygame_Setup.SCREEN, pygame_Setup.BLUE, (pygame_Setup.BLOCK_SIZE*node[1] + 4.5, pygame_Setup.BLOCK_SIZE*node[0] + 73, pygame_Setup.BLOCK_SIZE - 10, pygame_Setup.BLOCK_SIZE - 10))
                                pygame.display.flip()
                            solved = True
                        #A* Search
                        elif algorithmChoice == "A* Search":
                            a, path, spaceSearch = AStar(grid, AStarNode(startCoordinates), AStarNode(endCoordinates))
                            #Shows the search space by adding it to the grid
                            for node in spaceSearch:
                                grid[node.get_position()[0]][node.get_position()[1]] = '_'
                                pygame.display.flip()
                            #Shows the path by adding it to the grid
                            for node in path:
                                grid[node[0]][node[1]] = 'o'
                                pygame.draw.rect(pygame_Setup.SCREEN, pygame_Setup.BLUE, (pygame_Setup.BLOCK_SIZE*node[1] + 4.5, pygame_Setup.BLOCK_SIZE*node[0] +73, pygame_Setup.BLOCK_SIZE - 10, pygame_Setup.BLOCK_SIZE - 10))
                                pygame.display.flip()
                            solved = True
                        #Breadth First Search
                        elif algorithmChoice == "Breadth First Search":
                            for i in range(len(grid)):
                                for j in range(len(grid[0])):
                                    graph[i][j] = grid[i][j]
                            path, spaceSearch = BreadthFirst(graph, Node(startCoordinates), Node(endCoordinates))
                            #Shows the search space by adding it to the grid
                            for node in spaceSearch:
                                grid[node.get_position()[0]][node.get_position()[1]] = '_'
                                pygame.display.flip()
                            #Shows the path by adding it to the grid
                            for node in path:
                                grid[node[0]][node[1]] = 'o'
                                pygame.draw.rect(pygame_Setup.SCREEN, pygame_Setup.BLUE, (pygame_Setup.BLOCK_SIZE*node[1] + 4.5, pygame_Setup.BLOCK_SIZE*node[0] +73, pygame_Setup.BLOCK_SIZE - 10, pygame_Setup.BLOCK_SIZE - 10))
                                pygame.display.flip()
                            solved = True
                    else:
                        #Resets the grid once "visualised" has been pressed so the algorithm can be visualised again
                        for i in range(len(grid)):
                            for j in range(len(grid[0])):
                                if grid[i][j] == '_' or grid[i][j] == 'o':
                                    grid[i][j] = ' '
                        grid[startCoordinates[0]][startCoordinates[1]] = '*'
                        grid[endCoordinates[0]][endCoordinates[1]] = '*'
                        pygame_Setup.createVisualGrid(grid)
                        pygame.display.flip()
                        solved = False
            pygame.event.get()
    
    elif y >= menuHeight and dropdown.getIsDropdownDown() == False and solved == False and y >= 70:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame_Setup.SCREEN.get_at((x,y)) == (255, 255, 255):
                #Drawing the start node
                if numberOfPoints == 0:
                    startCoordinates = ((y-70)//pygame_Setup.BLOCK_SIZE, x//pygame_Setup.BLOCK_SIZE)
                    grid[(y-70)//pygame_Setup.BLOCK_SIZE][x//pygame_Setup.BLOCK_SIZE] = "*"
                    numberOfPoints += 1
                #Drawing the end node
                elif numberOfPoints == 1:
                    endCoordinates = ((y-70)//pygame_Setup.BLOCK_SIZE, x//pygame_Setup.BLOCK_SIZE)
                    grid[(y-70)//pygame_Setup.BLOCK_SIZE][x//pygame_Setup.BLOCK_SIZE] = "*"
                    numberOfPoints += 1
                #Drawing the walls
                elif numberOfPoints >=2 and wallsPlacable == True:
                    if grid[(y-70)//pygame_Setup.BLOCK_SIZE][x//pygame_Setup.BLOCK_SIZE] != "*":
                        grid[(y-70)//pygame_Setup.BLOCK_SIZE][x//pygame_Setup.BLOCK_SIZE] = "•"
                        numberOfPoints += 1
        pygame_Setup.createVisualGrid(grid)

    else:
        pygame.event.get()
    menu.drawMenu()
    pygame.display.update()
