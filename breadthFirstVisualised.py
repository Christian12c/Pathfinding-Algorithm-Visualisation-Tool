#Importing modules, procedures and constants that are referenced in this file
import pygame
import sys
from pygame_Setup import SCREEN, WHITE, BLACK, GREY, GREEN, RED, PURPLE, BLUE, BLOCK_SIZE
from node import Node
from my_queue import Queue
from stack import Stack

#Initialises all imported pygame modules
pygame.init()

def BreadthFirst(graph, start, end):
    queue = Queue()
    path = Stack()
    endPath = []
    spaceSearch = []
    visited = []

    #Iterates through each element in the 2D arry and creates an AStarNode depending on the contents of the element
    for i in range(len(graph)):
        for j in range(len(graph[1])):
            cell = Node((i,j))
            if graph[i][j] == '•':
                cell.set_traversable(False)
            graph[i][j] = cell
    #Initialises the discovered attribute of the start Node to True
    graph[start.get_position()[0]][start.get_position()[1]].set_discovered(True)
    pygame.draw.rect(SCREEN, BLUE, (BLOCK_SIZE*start.get_position()[1] + 1.5, BLOCK_SIZE*start.get_position()[0] + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))

    found = False
    enclosed = False
    queue.Enqueue(start)
    while len(queue.array) != 0 and found == False and enclosed == False:
        #Dequeues a Node wassigns it to currentNode
        currentNode = queue.Dequeue()
        if currentNode.get_position() == end.get_position():
            found = True
        pygame.event.get()

        visited.append(currentNode)
        neighbours = currentNode.listAllNeighbours(fullList=False)

        '''
        Checks if the start AStarNode is enclosed by walls.
        It works because the currentNode should be a neighbour of at least one of the AStarNodes that the algorithm has visited.
        This section checks if the currentNode is a neighbour of any of the AStarNodes in the array visited
        '''
        enclosed = True
        for i in visited:
            visitedNeighbours = i.listAllNeighbours()
            if currentNode.get_position() in visitedNeighbours or currentNode.get_position() == start.get_position():
                enclosed = False
        if enclosed == True:
            break

        #Copies the nodes in priorityQueue.array and endMinimumHeap.array that have the same position as the neighbours to listOfAllNeighbourNodes
        #This is needed as the listOfAllNeighbour method only returns an array of the positions not of AStarNodes so the corresponding AStarNodes have to be found
        listOfAllNeighbourNodes = []
        for i in range(len(graph)):
            for j in range(len(graph[1])):
                if graph[i][j].get_position() in neighbours:
                    listOfAllNeighbourNodes.append(graph[i][j])

        #Iterates through all the neighbours of currentNode
        for neighbourNode in listOfAllNeighbourNodes:
            #This means that the node is a wall
            if neighbourNode.get_traversable() == False:
                pass
            elif neighbourNode.get_discovered() == False and found == False:
                neighbourNodeColour = SCREEN.get_at((BLOCK_SIZE*neighbourNode.get_position()[1] + 2, BLOCK_SIZE*neighbourNode.get_position()[0] + 71))
                if neighbourNodeColour != BLUE:
                    pygame.draw.rect(SCREEN, GREEN, (BLOCK_SIZE*neighbourNode.get_position()[1] + 1.5, BLOCK_SIZE*neighbourNode.get_position()[0] + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
                    spaceSearch.append(neighbourNode)#The algorithm has "searched" neighbourNode so the neighbourNode is added to an array so it is saved
                pygame.display.flip()

                #Sets the neighbourNode to discovered and enqueues it
                for i in range(len(graph)):
                    for j in range(len(graph[1])):       
                        if graph[i][j].get_position() == neighbourNode.get_position():
                            graph[i][j].set_discovered(True)
                            queue.Enqueue(graph[i][j])
                            graph[i][j].set_parent(currentNode)
                            
    #The following section creates endPath by pushing successive parents of AStarNodes, starting from end, until start to get the shortest path     
    for i in range(len(graph)):
        for j in range(len(graph[1])):
            if graph[i][j].get_position() == end.get_position():
                path.Push(graph[i][j])
    node = path.array[0]
    while node.get_position() != start.get_position():
        parent = node.get_parent()
        path.Push(node)
        node = parent

    while len(path.array) > 0:
       endPath.append(path.Pop().get_position())
    endPath.append(start.get_position())
    
    return endPath, spaceSearch
