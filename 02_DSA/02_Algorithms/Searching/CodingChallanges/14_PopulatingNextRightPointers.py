# Populating Next Right Pointers in Each Node

# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children.

# populate each next pointer to point to its next right node. If there is no next right, the next pointer should be set to Null

class TreeNode():
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
        self.next = None

def BFS(queue):
    while queue:
        currentNode = None
        for i in range(len(queue)):
            prevNode = currentNode
            currentNode = queue.pop(0)
            if prevNode:
                prevNode.next = currentNode
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(1)
tree1.right = TreeNode(7)
tree1.right.left = TreeNode(6)
tree1.right.left.left = TreeNode(4)

q = []
q.append(tree1)
print(BFS(q, []))

print(tree1.left.next.value)