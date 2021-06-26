#Importing modules, procedures that are referenced in this file
import math
from time import sleep

gridWidth = 50
gridHeight = 20
#position = (y,x)

class Node:
    def __init__(self, position):
        self.__position = position
        self.__parent = None
        self.__distanceToStart = float('inf')
        self.__traversable = True
        self.__discovered = False

    #Get and set method for private attributes
    def get_position(self):
        return self.__position
    def set_position(self, x):
        self.__position = x
    def get_parent(self):
        return self.__parent
    def set_parent(self, x):
        self.__parent = x
    def get_distanceToStart(self):
        return self.__distanceToStart
    def set_distanceToStart(self, x):
        self.__distanceToStart = x
    def get_traversable(self):
        return self.__traversable
    def set_traversable(self, x):
        self.__traversable = x
    def get_discovered(self):
        return self.__discovered
    def set_discovered(self, x):
        self.__discovered = x

    #Finds the pythagorean distance from the node to another
    def lengthToOtherNode(self, node):
        return math.sqrt((self.__position[0] - node.__position[0])**2 + (self.__position[1] - node.__position[1])**2)

    #Returns all the positions of the neighbours of that node
    def listAllNeighbours(self, fullList=True):
        listOfAllNeighbours  = []

        #These are the neighbours to the "north", "east", "south" and "west"
        if self.__position[0] >= 0 and self.__position[0] < gridHeight  and self.__position[1] >= 0 and self.__position[1] < gridWidth:
            if self.__position[0] != 0:                                                      #North neighbour
                listOfAllNeighbours.append((self.__position[0]-1, self.__position[1]))
            if self.__position[1] != gridWidth - 1:                                          #East neighbour
                listOfAllNeighbours.append((self.__position[0], self.__position[1]+1))
            if self.__position[0] != gridHeight - 1:                                         #South neighbour
                listOfAllNeighbours.append((self.__position[0]+1, self.__position[1]))
            if self.__position[1] != 0:                                                      #West neighbour
                listOfAllNeighbours.append((self.__position[0], self.__position[1]-1))

            #This is adds the "NE", "SE", "SW" and "NW" neighbours
            if fullList:
                if self.__position[0] != 0 and self.__position[1] != 0:                          #North East neighbour
                    listOfAllNeighbours.append((self.__position[0] - 1 , self.__position[1] - 1))
                if self.__position[0] != gridHeight - 1 and self.__position[1] != gridWidth - 1: #South East neighbour
                    listOfAllNeighbours.append((self.__position[0] + 1 , self.__position[1] + 1))
                if self.__position[0] != 0 and self.__position[1] != gridWidth - 1:              #South West neighbour
                    listOfAllNeighbours.append((self.__position[0] - 1 , self.__position[1]+ 1))
                if self.__position[0] != gridHeight - 1 and self.__position[1] != 0:             #North West neighbour
                    listOfAllNeighbours.append((self.__position[0] + 1 , self.__position[1]- 1))
            return listOfAllNeighbours
        else:
            return []

class AStarNode(Node):
    def __init__(self, position):
        Node.__init__(self, position)
        super().__init__(position)

        self.__gCost = float('inf')
        self.__hCost = 0
        self.__fCost = float('inf')
        
    ##Inherited methods
    def get_position(self):
        return super().get_position()
    def set_position(self, x):
        super().set_position(x)
    def get_parent(self):
        return super().get_parent()
    def set_parent(self, x):
        super().set_parent(x)
    def get_traversable(self):
        return super().get_traversable()
    def set_traversable(self, x):
        super().set_traversable(x)
    def get_discovered(self):
        return super().get_discovered()
    def set_discovered(self, x):
        super().set_discovered(x)
    def lengthToOtherNode(self, node):
        return super().lengthToOtherNode(node)
    def listAllNeighbours(self):
        return super().listAllNeighbours()
    def get_gCost(self):
        return self.__gCost
    def set_gCost(self, x):
        self.__gCost = x
    def get_hCost(self, end):
        return super().lengthToOtherNode(end)
    def set_hCost(self, x):
        self.__hCost = x
    def get_fCost(self):
        return self.__fCost
    def set_fCost(self, x):
        self.__fCost = x
