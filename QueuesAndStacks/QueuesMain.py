# FIFO //First in First Out
# example: people in the queue of roller coaster 

# lookup O(n)
# enqueue O(1) //add
# dequeue O(1) //remove
# peek O(1) //View the last element

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.last
    
    def enqueue(self,val):
        newNode = Node(val)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self
    
    def dequeue(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.last = None

        self.first = self.first.next
        self.length -= 1
        return self

    def printQueue(self):
        currentNode = self.first 
        while currentNode != None and currentNode.value:
            print(currentNode.value)
            currentNode = currentNode.next

myQueue = Queue()
myQueue.enqueue('FirstPerson')
myQueue.enqueue('SecondPerson')
myQueue.enqueue('ThirdPerson')
myQueue.enqueue('ForthPerson')
myQueue.printQueue()
print('-------------------')
myQueue.dequeue()
myQueue.printQueue()
print(myQueue.peek().value)
