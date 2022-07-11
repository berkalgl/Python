# Given the root of a binary tree and an integer targetSum. return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum
class TreeNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def BFS(queue):
    while queue:
        for i in range(len(queue)):
            currentNode = queue.pop(0)

            if currentNode.left == None and currentNode.right == None:
                if currentNode.value == 0:
                    return True

            if currentNode.left:
                currentNode.left.value = currentNode.value - currentNode.left.value
                queue.append(currentNode.left)

            if currentNode.right:
                currentNode.right.value = currentNode.value - currentNode.right.value
                queue.append(currentNode.right)
    
    return False

tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(1)
tree1.right = TreeNode(7)
tree1.right.left = TreeNode(6)
tree1.right.left.left = TreeNode(4)

targetSum = 9
tree1.value = targetSum - tree1.value
q = []
q.append(tree1)
print(BFS(q))