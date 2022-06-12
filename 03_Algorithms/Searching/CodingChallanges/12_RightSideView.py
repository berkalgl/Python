# given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom

class TreeNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def BFS(queue, rightSideList):
    while queue:
        for i in range(len(queue)):
            currentNode = queue.pop(0)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        rightSideList.append(currentNode.value)
    return rightSideList

tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(1)
tree1.right = TreeNode(7)
tree1.right.left = TreeNode(6)

q = []
q.append(tree1)
print(BFS(q, []))