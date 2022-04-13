# myLinkedList = {
#     'value': 10,
#     'next': {
#         'value': 5,
#         'next': {
#             'value': 16,
#             'next': None
#         }
#     }
# }

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head
        self.length = 1
    
    def append(self,val):
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def preprend(self,val):
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead
        self.length += 1
        return self

    def insert(self, index, val):
        if index == 0:
            self.preprend(val)
            return self
        
        if index >= self.length:
            self.append(val)
            return self

        newNode = Node(val)
        leader = self.getNodeByIndex(index-1)

        newNode.next = leader.next
        leader.next = newNode
        self.length += 1

        return self

    def getNodeByIndex(self, index):
        if index >= self.length:
            return self.tail

        currentNode = self.head
        currentIndex = 0
        while index != currentIndex:
            currentNode = currentNode.next
            currentIndex += 1

        return currentNode

    def printList(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

        
myLinkedList = LinkedList(10)
myLinkedList.append(6)
myLinkedList.append(4)
myLinkedList.append(8)
myLinkedList.printList()
print('-----------')
myLinkedList.insert(2,20)
myLinkedList.printList()
print('-----------')
myLinkedList.insert(99,20)
myLinkedList.printList()
# print(myLinkedList.length)
# print('-----------')
# myLinkedList.preprend(1)
# myLinkedList.printList()
# print(myLinkedList.length)