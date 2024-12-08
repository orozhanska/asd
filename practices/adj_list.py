# Adjascency List representation in Python 
# V1

class Node:
    def __init__(self, data):
        self.data = data


class Graph:
    def __init__(self):
        # Adjacency list representation: each list represents the neighbors of a node
        self.alist = []

    def add_node(self, node):
        # Each node starts with its own list of neighbors (empty initially)
        self.alist.append([node])

    def add_edge(self, src, dst):
        # Add a reference to the destination node in the source node's adjacency list
        src_list = self.alist[src]
        dst_node = self.alist[dst][0]
        src_list.append(dst_node)
        # directed graph
    def check_edge(self, src, dst):
        # Check if the destination node exists in the source node's adjacency list
        src_list = self.alist[src]
        dst_node = self.alist[dst][0]
        return dst_node in src_list

    def print_graph(self):
        # Print each node and its adjacency list
        for current_list in self.alist:
            for node in current_list:
                print(node.data, end=" -> ")
            print()


# Main
if __name__ == "__main__":
    # Create the graph
    graph = Graph()

    # Add nodes
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

    # Print the graph
    graph.print_graph()

    # Check if an edge exists
    # print(graph.check_edge(0, 1))


# V2
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node
        # undirected graph
        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()

print([[0] * 5 for _ in range(2)])