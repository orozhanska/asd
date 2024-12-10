# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')


# or inside the adjacency matrix
class Node:
    def __init__(self, data):
        self.data = data


class Graph:
    def __init__(self, size):
        # Initialize the graph with an adjacency matrix
        self.nodes = []
        self.matrix = [[0] * size for _ in range(size)]

    def add_node(self, node):
        # Add a node to the graph
        self.nodes.append(node)

    def add_edge(self, src, dst):
        # Add a directed edge from src to dst
        self.matrix[src][dst] = 1

    def check_edge(self, src, dst):
        # Check if an edge exists between src and dst
        return self.matrix[src][dst] == 1

    def print_graph(self):
        # Print the adjacency matrix
        print("  ", end="")
        for node in self.nodes:
            print(node.data, end=" ")
        print()
        for i, row in enumerate(self.matrix):
            print(self.nodes[i].data, end=" ")
            print(" ".join(map(str, row)))
        print()

    def depth_first_search(self, src):
        # Perform a depth-first search starting from the given source node
        visited = [False] * len(self.matrix)
        self._dfs_helper(src, visited)

    def _dfs_helper(self, src, visited):
        # Helper function for DFS
        if visited[src]:
            return
        visited[src] = True
        print(f"{self.nodes[src].data} = visited")
        for i in range(len(self.matrix[src])):
            if self.matrix[src][i] == 1:
                self._dfs_helper(i, visited)


# Main
if __name__ == "__main__":
    # Initialize the graph with 5 nodes
    graph = Graph(5)

    # Add nodes to the graph
    graph.add_node(Node('A'))
    graph.add_node(Node('B'))
    graph.add_node(Node('C'))
    graph.add_node(Node('D'))
    graph.add_node(Node('E'))

    # Add edges
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(4, 0)
    graph.add_edge(4, 2)

    # Print the adjacency matrix
    graph.print_graph()

    # Perform depth-first search starting from node 0 (A)
    graph.depth_first_search(0)

