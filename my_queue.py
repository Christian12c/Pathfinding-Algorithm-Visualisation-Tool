#Creates a class for a queue
class Queue:
    def __init__(self):
        self.array = []
        self.top = 0
        self.rear = -1

    #Enqueues an object
    def Enqueue(self, value):
        self.rear += 1
        self.array.append(value)

    #Dequeues an object
    def Dequeue(self):
        if len(self.array) > 0:
            topValue = self.array[0]
            self.array.pop(0)
            return topValue
        else:
            return -1
