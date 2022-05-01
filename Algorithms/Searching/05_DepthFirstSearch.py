# The search follows one branch of the tree down as many levels as possible until the target notice found or the end is reached
# when the search can go on any further, it continues at the nearest ancestor with an unexplored child.

#          9
#       6     12
#      1 4   34 45

# 9 --> 6 --> 1 when reached the leaf node, then goes up to 6 and check if there is node that is not visited
# 6 --> 4 --> 9
# 12 --> 34 --> 12 --> 45
# dfs has a lower memory requirement than bfs because it is not necessary to store all the child pointers
# at each level, something that we will see when we actually coded
#        9
#    4      20
#  1   6  15   170
#[9,4,1,6,20,15,170]

# 3 way to implement it
# in order [1,4,6,9,15,20,170]
# pre order[9,4,1,6,20,15,170]
# post order [1,6,4,15,170,20,9]

#MEMORY CONSUMPTION O(high of the tree)

# importing sys
import sys
  
sys.path.insert(0, 'D:/CodeRepository/PythonDSA')
from DataStructures.Trees.TreesMain import BinarySearchTree

class DepthFirstSearch:
    def __init__(self, tree:BinarySearchTree):
        self.tree = tree
    ### IN ORDER
    def TraverseInOrder(self,node, result):
        print(node.value)
        if node.left:
            self.TraverseInOrder(node.left,result)

        result.append(node.value)

        if node.right:
            self.TraverseInOrder(node.right,result)

        return result

    # most of the time this search implemented with recursive 
    def DepthFirstSearchInOrder(self):
        return self.TraverseInOrder(self.tree.root, [])
    
    ### PRE ORDER
    def TraversePreOrder(self,node, result):
        result.append(node.value)
        if node.left:
            self.TraversePreOrder(node.left,result)

        if node.right:
            self.TraversePreOrder(node.right,result)

        return result

    def DepthFirstSearchPreOrder(self):
        return self.TraversePreOrder(self.tree.root, [])

    ### POST ORDER
    def TraversePostOrder(self,node, result):
        if node.left:
            self.TraversePostOrder(node.left,result)

        if node.right:
            self.TraversePostOrder(node.right,result)

        result.append(node.value)
        return result

    def DepthFirstSearchPostOrder(self):
        return self.TraversePostOrder(self.tree.root, [])
        
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

dfs = DepthFirstSearch(myTree)

print(dfs.DepthFirstSearchInOrder())
print('-----------------------')
print(dfs.DepthFirstSearchPreOrder())
print('-----------------------')
print(dfs.DepthFirstSearchPostOrder())