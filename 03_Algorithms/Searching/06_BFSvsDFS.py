# they both traverse, but each one is used for different purpose
# Both are O(n)

# BFS adv disadv
# Shortest Path          More memory
# Closer Nodes
# if you have additional information on the location of the target node and you know that the node is likely
# in the upper level of a tree, then bfs is better because it will search through the closest nodes first

# DFS
# Less memory       Can get slow
# Does Path Exist ? 
# if the additional information provides that the target node is at the lower level
# dfs is better

# https://stackoverflow.com/questions/9844193/what-is-the-time-and-space-complexity-of-a-breadth-first-and-depth-first-tree-tr

# Exercise >>> !Important
#If you know a solution is not far from the root of the tree:
# BFS

#If the tree is very deep and solutions are rare: 
# BFS (we have memory concern though) (DFS will take long time)

#If the tree is very wide:
# DFS (BFS will need too much memory)

#If solutions are frequent but located deep in the tree:
# DFS

#Determining whether a path exists between two nodes:
# DFS

#Finding the shortest path:
# BFS