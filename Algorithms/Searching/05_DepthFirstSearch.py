# The search follows one branch of the tree down as many levels as possible until the target notice found or the end is reached
# when the search can go on any further, it continues at the nearest ancestor with an unexplored child.

#          9
#       6     12
#      1 4   34 45

# 9 --> 6 --> 1 when reached the leaf node, then goes up to 6 and check if there is node that is not visited
# 6 --> 4 --> 9
# 12 --> 34 --> 12 --> 45
# dfs has a lower memory requirement than bfs because it is not necessary to store all the child pointers
# at each level, something that we will see when we actually coded
#        9
#    4      20
#  1   6  15   170
[9,4,1,6,20,15,170]