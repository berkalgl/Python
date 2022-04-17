# LIFO //Last in First Out
# 
# lookup O(n)
# pop O(1) //remove
# push O(1) //add
# peek O(1) //View the last element

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.bottom = newNode
            self.top = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer

        self.length += 1

        return self


    def pop(self):
        self.top = self.top.next
        self.length -= 1
        return self
    
    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def printStack(self):
        currentItem = self.top
        while currentItem != None and currentItem.value:
            print(currentItem.value)
            currentItem = currentItem.next


myStack = Stack()
myStack.push('Google')
myStack.push('Turkcell')
myStack.push('Garanti')
myStack.push('Vodafone')
myStack.printStack()
print('------------')
myStack.pop()
myStack.printStack()
print(myStack.top.value)
print(myStack.length)
