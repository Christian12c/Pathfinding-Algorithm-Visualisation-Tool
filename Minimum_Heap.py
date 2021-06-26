#Importing modules, procedures and constants that are referenced in this file
from node import Node
from node import AStarNode

class MinimumHeap:
    def __init__(self):
        self.array = []

    #A recursive method that sorts the heap
    def Heapify(self, parentIndex):
        smallest = parentIndex
        if parentIndex == 0:
            leftChildIndex, rightChildIndex = 1, 2
        else:
            leftChildIndex = 2 * parentIndex
            rightChildIndex = 2 * parentIndex + 1

        #Checks if the parent node is smaller than its children
        if leftChildIndex >=0 and leftChildIndex < len(self.array):
            if self.array[leftChildIndex].get_distanceToStart() < self.array[smallest].get_distanceToStart():
                smallest = leftChildIndex
        if rightChildIndex >= 0 and rightChildIndex < len(self.array):
            if self.array[rightChildIndex].get_distanceToStart() < self.array[smallest].get_distanceToStart():
                smallest = rightChildIndex

        #If the parent node is not the smallest then it get swapped with the parent's smallest node then Heapify is recursively called
        if smallest != parentIndex:
            self.array[smallest], self.array[parentIndex] = self.array[parentIndex], self.array[smallest]
            self.Heapify(smallest)

    #Decreases the node's distanceToStart and then sorts itself the heap
    def DecreaseKey(self, index, key):
        self.array[index] = key
        while(index > 0 and self.array[index//2].get_distanceToStart() > self.array[index].get_distanceToStart()):
            self.array[index], self.array[index//2] = self.array[index//2], self.array[index]
            index = index//2

    #Adds a node to the minimum heap
    def Insert(self, key):
        self.array.append(key)
        self.DecreaseKey(len(self.array) - 1, key)

    #Extracts the node with the smallest distanceToStart attribute
    def ExtractMinimum(self):
        minimum = self.array[0]
        self.array[0] = self.array[len(self.array) - 1]
        self.array.pop()
        self.Heapify(0)
        return minimum

    #Returns the index of the node in the array
    def IndexOf(self, node):
        for i in range(len(self.array)):
            if self.array[i].get_position() == node.get_position():
                return i
        return -1

class AStarMinimumHeap(MinimumHeap):
    #An inherited method
    def __init__(self):
        MinimumHeap.__init__(self)
        super().__init__()

    #An overrided method (polymorphism)       
    def Heapify(self, parentIndex):
        smallest = parentIndex
        if parentIndex == 0:
            leftChildIndex, rightChildIndex = 1, 2
        else:
            leftChildIndex = 2 * parentIndex
            rightChildIndex = 2 * parentIndex + 1
            
        if(leftChildIndex >=0 and leftChildIndex < len(self.array)):
            if(self.array[leftChildIndex].get_fCost() < self.array[smallest].get_fCost()):
                smallest = leftChildIndex
        if(rightChildIndex >= 0 and rightChildIndex < len(self.array)):
            if(self.array[rightChildIndex].get_fCost() < self.array[smallest].get_fCost()):
                smallest = rightChildIndex

        if(smallest != parentIndex):
            self.array[smallest], self.array[parentIndex] = self.array[parentIndex], self.array[smallest]
            self.Heapify(smallest)

    #An overrided method (polymorphism)       
    def DecreaseKey(self, index, key):
        self.array[index] = key
        while(index > 0 and self.array[index//2].get_fCost() > self.array[index].get_fCost()):
            self.array[index], self.array[index//2] = self.array[index//2], self.array[index]
            index = index//2

    #An inherited method
    def Insert(self, key):
        super().Insert(key)

    #An inherited method
    def ExtractMinimum(self):
        return super().ExtractMinimum()

    #An inherited method
    def IndexOf(self, node):
        return super().IndexOf(node)
