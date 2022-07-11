'''
Given the root of a binary tree, invert the tree, and return its root.
https://leetcode.com/problems/invert-binary-tree/
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert(root):
    queue = []

    if root:
        queue.append(root)

    while queue:
        curr = queue.pop(0)

        curr.left, curr.right = curr.right, curr.left

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)


def invertWithDFS(root):

    if not root:
        return None

    root.left, root.right = root.right, root.left

    if root.left:
        invertWithDFS(root.left)
    
    if root.right:
        invertWithDFS(root.right)

    return root