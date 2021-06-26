#Creates a class for a stack 
class Stack:
    def __init__(self):
        self.array = []

    #Pushes an object
    def Push(self, value):
        self.array.append(value)

    #Pops an object
    def Pop(self):
        if len(self.array) > 0:
            top = self.array[len(self.array)-1]
            self.array.pop()
            return top
        else:
            return -1
