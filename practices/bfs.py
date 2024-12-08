graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling

print()

from collections import deque

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

    def breadth_first_search(self, src):
        # Perform a breadth-first search starting from the given source node
        queue = deque()
        visited = [False] * len(self.matrix)

        queue.append(src)
        visited[src] = True

        while queue:
            current = queue.popleft()
            print(f"{self.nodes[current].data} = visited")

            for i in range(len(self.matrix[current])):
                if self.matrix[current][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True


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

    # Perform breadth-first search starting from node 0 (A)
    graph.breadth_first_search(0)
