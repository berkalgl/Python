# LIFO //Last in First Out
# 
# lookup O(n)
# pop O(1) //remove
# push O(1) //add
# peek O(1) //View the last element

# STACKS WITH LINKED LIST

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
        if self.top == None:
            return None

        if self.top == self.bottom:
            self.bottom = None

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


# myStack = Stack()
# myStack.push('Google')
# myStack.push('Turkcell')
# myStack.push('Garanti')
# myStack.push('Vodafone')
# myStack.printStack()
# print('------------')
# myStack.pop()
# myStack.printStack()
# print(myStack.peek().value)
# print(myStack.length)
#-------------------------
# STACKS WITH ARRAY

class StackArray:
    def __init__(self):
        self.data = []

    def peek(self):
        return self.data[len(self.data)-1]

    def push(self, val):
        self.data.append(val)
        return self

    def pop(self):
        self.data.pop()
        return self
    
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False

    def printStack(self):
        for i in range(len(self.data)-1,-1,-1):
            print(self.data[i])

stackWithArray = StackArray()
stackWithArray.push('Google')
stackWithArray.push('Google1')
stackWithArray.push('Google2')
stackWithArray.printStack()
print('------------------')
stackWithArray.pop()
stackWithArray.printStack()


