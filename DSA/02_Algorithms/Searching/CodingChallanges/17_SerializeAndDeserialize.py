# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or trasmitted across a network connection link
# to be reconstructed later in the same or another computer environment

# design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm 
# should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the orginal tree structure.

#Serialize a tree

class TreeNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def Serialize(queue, list):
    while queue:
        for i in range(len(queue)):
            curr = queue.pop(0)

            if curr.left:
                queue.append(curr.left)
                list.append(curr.left.value)
            else:
                list.append(None)
                
            if curr.right:
                queue.append(curr.right)
                list.append(curr.right.value)
            else:
                list.append(None)
    return list


tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(4)
tree1.right = TreeNode(8)
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(9)

q = []
q.append(tree1)
list1 = []
list1.append(tree1.value)
print(Serialize(q, list1))

def Deserialize(queue, list):
    j = 1

    while queue:
        for i in range(len(queue)):
            curr = queue.pop(0)

            if list[j] != None:
                curr.left = TreeNode(list[j])
                queue.append(curr.left)
            else:
                curr.left = None
            
            j += 1
            if list[j] != None:
                curr.right = TreeNode(list[j])
                queue.append(curr.right)
            else:
                curr.right = None

