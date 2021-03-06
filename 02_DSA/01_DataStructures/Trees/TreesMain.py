# dom in html page is a tree data structure
# having a computer making a decision in a chees game is also a tree data structure
# facebook comments are too
# abstract syntax tree is used by computers run any code

# BINARY TREES
# Each node can only have either zero one or two nodes and each child can only have one parent
# Perfect Binary Tree has no leaf left one // Number of bottom nodes = number of top nodes + 1, that means half of the nodes stands at the bottom
# Full Binary Tree has at least one node left alone with no children

# balanced                  unbalanced #keep adding to the right or left
# lookup O(logN)            lookup O(n)
# insert O(logN)            insert O(n)
# delete O(logN)            delete O(n)

# BST
# Advantages                Disadvantages
# Better than O(n)          No O(1) Operations
# Ordered
# Flexible size

# to balance the binary search tree, we can use AVL and Red Black Trees
# AVL
# https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
# https://medium.com/basecs/the-little-avl-tree-that-could-86a3cae410c7

# Red Black 
# https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
# https://medium.com/basecs/painting-nodes-black-with-red-black-trees-60eacb2be9a5

# Comparision 
# https://stackoverflow.com/questions/13852870/red-black-tree-over-avl-tree

# Level 0: 2^0 = 1
# Level 1: 2^1 = 2
# Level 2: 2^2 = 4
# Level 3: 2^3 = 8
# number of nodes = 2^h - 1  h: number of levels
# log nodes = height(Steps)     log100=2
# Google search uses binary tree, looking for a phone number in a phone book is a also binary search tree
#https://visualgo.net/en/bst

# BINARY SEARCH TREE

class BinaryTreeNode:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = BinaryTreeNode(val)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if newNode.value < currentNode.value:
                    #left
                    if not currentNode.left:
                        currentNode.left = newNode
                        return self
                    currentNode = currentNode.left
                else:
                    #right
                    if not currentNode.right:
                        currentNode.right = newNode
                        return self
                    currentNode = currentNode.right

    def lookup(self, val):
        if self.root == None:
            return False

        currentNode = self.root
        while currentNode:
            if val == currentNode.value:
                return True

            if val < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        
        return False
    
    def remove(self,val):
        if self.root == None:
            return False
        
        currentNode = self.root
        parentNode = None
        while currentNode:
            if val < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif val > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif val == currentNode.value:
                #We have a match
                #Option 1: No right child
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        #if parent > current value, make current left child a child of parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        #if parent < current value, make curremt left child a right child of parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left
                #Option 2: right child which doesnt have a left child
                elif currentNode.right.left == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        currentNode.right.left = currentNode.left
                        #if parent > current, make right child of the left the parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                        #if parent < current, make right child a right child of the parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right
                #Option 3: right child that has a left child
                else:        
                    leftmost = currentNode.right.left
                    leftmostparent = currentNode.right
                    while leftmost.left != None:
                        leftmostparent = leftmost
                        leftmost = leftmost.left
                    
                    leftmostparent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
            return True

    def LeftViewOfTheBST(self):
        queue = []
        queue.append(self.root)
        result = []

        while len(queue):
            length = len(queue)
            for i in range(1, length + 1):
                curr_node = queue.pop(0)
                if i == 1: # to see the right view just equal to the size
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

print(myTree.LeftViewOfTheBST())
print(myTree.lookup(169))
print(myTree.remove(170))
