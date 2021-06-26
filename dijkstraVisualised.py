#Importing modules, procedures and constants that are referenced in this file
import pygame
import sys
from pygame_Setup import SCREEN, WHITE, BLACK, GREY, GREEN, RED, PURPLE, BLUE, BLOCK_SIZE
from Minimum_Heap import MinimumHeap
from node import Node
from stack import Stack

#Initialises all imported pygame modules
pygame.init()

def Dijkstra(graph, start, end):
    priorityQueue = MinimumHeap()
    endMinimumHeap = MinimumHeap()
    path = Stack()
    endPath = []
    spaceSearch = []
    visited = []

    #Iterates through each element in the 2D arry and creates a Node depending on the contents of the element
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            cell = Node((i,j))
            if graph[i][j] == '•':
                cell.set_traversable(False)
            priorityQueue.Insert(cell)
    #Initialises the distanceToStart of the start Node to 0
    #Changes the distanceToStart of a Node in the priority queue that has the same "position" as start
    start.set_distanceToStart(0)
    priorityQueue.DecreaseKey(start.get_position()[0]*len(graph[0])+start.get_position()[1], start)
    pygame.draw.rect(SCREEN, BLUE, (BLOCK_SIZE*start.get_position()[1] + 1.5, BLOCK_SIZE*start.get_position()[0] + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))

    '''
    A while loop that runs updating the distanceToStart of each Node in the graph until the priority queue is empty...
    ...or the end Node is found or the algorithm figures out that the start Node is "enclosed"
    '''
    found = False
    enclosed = False
    while len(priorityQueue.array) != 0 and found == False and enclosed == False:
        #Extracts the AStarNode with the smallest fCost and assigns it to currentNode
        currentNode = priorityQueue.ExtractMinimum()
        if currentNode.get_position() == end.get_position():
            found = True
        pygame.event.get()
        pygame.draw.rect(SCREEN, BLUE, (BLOCK_SIZE*start.get_position()[1] + 1.5, BLOCK_SIZE*start.get_position()[0] + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
        pygame.draw.rect(SCREEN, BLUE, (BLOCK_SIZE*end.get_position()[1] + 1.5, BLOCK_SIZE*end.get_position()[0] + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
        
        
        endMinimumHeap.Insert(currentNode)
        visited.append(currentNode)
        neighbours = currentNode.listAllNeighbours()

        '''
        Checks if the start Node is enclosed by walls.
        It works because the currentNode should be a neighbour of at least one of the Nodes that the algorithm has visited.
        This section checks if the currentNode is a neighbour of any of the AStarNodes in the array visited
        '''
        enclosed = True
        for i in visited:
            visitedNeighbours = i.listAllNeighbours()
            if currentNode.get_position() in visitedNeighbours or currentNode.get_position() == start.get_position():
                enclosed = False
        if enclosed == True:
            break

        
        listOfAllNeighbourNodes = []
        #Copies the nodes in priorityQueue.array and endMinimumHeap.array that have the same position as the neighbours to listOfAllNeighbours 
        #This is needed as the listOfAllNeighbour method only returns an array of the positions not of AStarNodes so the corresponding AStarNodes have to be found
        for i in priorityQueue.array:        
            if i.get_position() in neighbours:
                listOfAllNeighbourNodes.append(i)
        for i in endMinimumHeap.array:        
            if i.get_position() in neighbours:
                listOfAllNeighbourNodes.append(i)

        #Iterates through all the neighbours of currentNode
        for neighbourNode in listOfAllNeighbourNodes:
            #This means that the node is a wall
            if neighbourNode.get_traversable() == False:   ##NeigbourNode is just tuple eg (1,2) not a node
                pass
            else:
                if found == False and neighbourNode.get_position() != end.get_position():
                    pygame.draw.rect(SCREEN, GREEN, (BLOCK_SIZE*neighbourNode.get_position()[1] + 1.5, BLOCK_SIZE*neighbourNode.get_position()[0] + 70, BLOCK_SIZE - 3, BLOCK_SIZE - 3))
                    pygame.display.flip()
                spaceSearch.append(neighbourNode) #The algorithm has "searched" neighbourNode so the neighbourNode is added to an array so it is saved

                '''
                Compares the fCost of the neighbourNode and compares it to the alternativeDistance the algorithm has found
                If the alternativeDistance is smaller then the fCost, gCost and parent of the neighbourNode is updated
                '''
                alternativeDistance = currentNode.get_distanceToStart() + currentNode.lengthToOtherNode(neighbourNode)
                if alternativeDistance < neighbourNode.get_distanceToStart():
                    for i in priorityQueue.array:        
                        if i.get_position() == neighbourNode.get_position():
                            i.set_distanceToStart(alternativeDistance) ##Decrease the key ie distanceToStart
                            i.set_parent(currentNode)
                            priorityQueue.DecreaseKey(priorityQueue.IndexOf(i), i)

    #Returns without actually adding anything to the values being returned as there is no path        
    if enclosed == True:
            return endMinimumHeap, endPath, spaceSearch

    #The following section creates endPath by pushing successive parents of AStarNodes, starting from end, until start to get the shortest path     
    for i in endMinimumHeap.array:
        if i.get_position() == end.get_position():
            path.Push(i)

    node = path.array[0]
    while node.get_position() != start.get_position():
        parent = node.get_parent()
        path.Push(node)
        node = parent

    while len(path.array) > 1:
       endPath.append(path.Pop().get_position())
    
    return endMinimumHeap, endPath, spaceSearch
