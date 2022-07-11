# Maximum depth of a binary Tree

# Given the root of a binary tree, return its maximum depth
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def BFSCount(queue, count):
    while queue:
        for i in range(0, len(queue)): 
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        count += 1

    return count

tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(1)
tree1.right = TreeNode(7)
tree1.right.left = TreeNode(6)

q = []
q.append(tree1)
count = 0
print(BFSCount(q, count))

def MaxHeight(node):
    if node is None:
        return 0
    else:
        lDepth = MaxHeight(node.left)
        rDepth = MaxHeight(node.right)

        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


print(MaxHeight(tree1))
