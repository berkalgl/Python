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

# Advantages                Disadvantages
# Better than O(n)          No O(1) Operations
# Ordered
# Flexible size

# Level 0: 2^0 = 1
# Level 1: 2^1 = 2
# Level 2: 2^2 = 4
# Level 3: 2^3 = 8
# # of nodes = 2^h - 1  h: number of levels
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
print(myTree.lookup(169))
