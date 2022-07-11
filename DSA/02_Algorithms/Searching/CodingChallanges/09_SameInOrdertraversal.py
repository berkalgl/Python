# Check if trees are same inorder traversal

# Given two binary trees, determine whether
# they have the same inorder traversal.

#     Tree 1                    Tree2
#        5                        3
#      3   7                    1   6 
#     1   6                        5  7
#   1,3,5,6,7                 1,3,5,6,7

class TreeNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def traverse_in_order(node, list):
    if node == None:
        return
    
    if node.left:
        traverse_in_order(node.left, list)

    list.append(node.value)

    if node.right:
        traverse_in_order(node.right, list)

tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(1)
tree1.right = TreeNode(7)
tree1.right.left = TreeNode(6)

tree2 = TreeNode(3)
tree2.left = TreeNode(1)
tree2.right = TreeNode(6)
tree2.right.left = TreeNode(5)
tree2.right.right = TreeNode(7)

list1 = []
list2 = []

traverse_in_order(tree1, list1)

traverse_in_order(tree2, list2)

print(list1)
# ----------
print(list2)
# ----------
print(list1 == list2)