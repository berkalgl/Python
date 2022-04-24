# Graph is simply a set of values that are related in a pairwise fashion
# each item called node (vortex), every connection is called an edge
# networks, www, facebook social network, amazon recommodation, google short path for google maps

# Linked list are type of trees, trees are type of graphs

# they can be directed or undirected
# directed are oneway street, undirected you can go and go back
# adding friend on facebook is undirected
# however on twitter or instagram, following a person is directed graph

# weighted and unweighted graph
# weighted graphs contains values in their edges as well
# weighted graphs can help us to find the optimum paths 

# Cyclic and Acyclic graph
# you can go where you started in cyclic graph. every nodes has connection themselves

# favorite graph : https://internet-map.net

# https://visualgo.net/en/graphds?slide=1

# Directed acyclic graph --> DAG its so common. IOTA blockchain project uses this.

# Adv.              Disadv.
# relationships     scaling is hard
# neo4j lets us to build graphs 3rd party

#How to build ?
#1- Edge list
#   2-----0
#   | \
#   1--3
# Edge list shows us the connections
graph = [[0,2],[2,3],[2,1],[1,3]]

#2- Adjacent List 
# creating a graph where the index is the node and the value is the nodes neighbors
graph2 = [[2],[2,3],[0,1,3],[1,2]]

#3- Adjacent Matrix
#The matrix is simply going to have zeros and ones indicating whether the Node X has a connection to Node Y
# also we can use object
graph3 = [
    [0,0,1,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]
graph4 = {0 : [0,0,1,0],
          1 : [0,0,1,1],
          2 : [1,1,0,1],
          3 : [0,1,1,0]}

class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        if node1 in self.adjacentList:
            self.adjacentList[node1].append(node2)
        
        if node2 in self.adjacentList:
            self.adjacentList[node2].append(node1)

    
    def showConnection(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ''
            vertex = None
            for vertex in nodeConnections:
                connections += vertex + " "
            print(node + "-->" + connections)

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1') 
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')

myGraph.showConnection() 