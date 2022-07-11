# Given the root of a binary tree, check whether it is a mirror of itself

class TreeNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def BFS(queue):
    values = []
    while queue:
        for i in range(len(queue)):
            currentNode = queue.pop(0)
            if not currentNode:
                values.append(None)
            else:
                queue.append(currentNode.left)
                queue.append(currentNode.right)
                values.append(currentNode.value)
        
        #check if list symmetrical
        if not checkList(values):
            return False
        #clear list
        values = []

    return True

def checkList(values):
    start = 0
    end = len(values) - 1
    while start < end:
        if values[start] != values[end]:
            return False
        start += 1
        end -= 1
    return True

tree1 = TreeNode(5)
tree1.left = TreeNode(4)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(2)
tree1.right = TreeNode(4)
tree1.right.left = TreeNode(2)
tree1.right.right = TreeNode(1)

q = []
q.append(tree1)
print(BFS(q))


