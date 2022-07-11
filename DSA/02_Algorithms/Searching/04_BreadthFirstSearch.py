# searching starting with the root, and search line by line left to the right
#             1
#         2       3
#      4    5   6    7
# bfs uses additional memory because it is necessary to track the child nodes of all the nodes on a given level while searchin that level
#        9
#    4      20
#  1   6  15   170
# [9,4,20,1,6,15,170]

# importing sys
import sys
  
sys.path.insert(0, 'Users\berkalgul\Desktop\CodeRepository\PythonDSA')
from DataStructures. Trees.TreesMain import BinarySearchTree
from DataStructures.QueuesAndStacks.QueuesMain import Queue

def BreadthFirstSearch(searchTree:BinarySearchTree):
    currentNode = searchTree.root
    result = []
    queue = Queue()
    queue.enqueue(currentNode)

    while queue.length > 0:
        currentNode = queue.dequeue()
        result.append(currentNode.value.value)
        if currentNode.value.left:
            queue.enqueue(currentNode.value.left)
        if currentNode.value.right:
            queue.enqueue(currentNode.value.right)

    return result

def BreadthFirstSearchRecursive(queue:Queue, result):
    if queue.length == 0:
        return result

    currentNode = queue.dequeue()
    result.append(currentNode.value.value)
    if currentNode.value.left:
        queue.enqueue(currentNode.value.left)
    if currentNode.value.right:
        queue.enqueue(currentNode.value.right)

    return BreadthFirstSearchRecursive(queue, result)

def LeftViewOfTheBST(searchTree:BinarySearchTree):
    queue = []
    queue.append(searchTree.root)
    result = []

    while not len(queue):
        length = len(queue)
        for i in range(1, length):
            curr_node = queue.pop(0)
            if i == 1:
                result.append(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    return result

    
    
#        9
#    4      20
#  1   6  15   170

myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(1)
myTree.insert(6)
myTree.insert(15)
myTree.insert(170)

print(BreadthFirstSearch(myTree))
print('-----------------------')
print(BreadthFirstSearchRecursive(Queue.enqueue(Queue(),myTree.root), []))
print('-----------------------')
print(LeftViewOfTheBST(myTree))