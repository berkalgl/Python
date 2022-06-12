# Given the root of a binary tree, return the leftmost value in the last row of the tree

class TreeNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def BFS(queue):
    currentNode = None
    while queue:
        for i in range(len(queue)):
            currentNode = queue.pop(0)
            if currentNode.right:
                queue.append(currentNode.right)
            if currentNode.left:
                queue.append(currentNode.left)
    
    return currentNode.value
                
tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(1)
tree1.right = TreeNode(7)
tree1.right.left = TreeNode(6)
tree1.right.left.left = TreeNode(4)

q = []
q.append(tree1)
print(BFS(q))