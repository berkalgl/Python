# Dijkstra and Bellman-Ford Algorithms

# they are used for finding shortest path. BFS assumes that each jump to another node in a graph which unweighted. same with dfs
# DFS and BFS does not care about the edges.

# https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e

# Bellmen ford is very effective at solving the shortest path over Dijkstra
# because it can accommodate negative weights. It can solve the shortest path within graph which has negative edges
# However, Bellmen ford can take a really long time in the name of complexity. It is O(n^2).
# Dijkstra is faster, and more efficient. With the downside that it can accommodate for negative weights