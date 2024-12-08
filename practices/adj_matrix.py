class Node:
    def __init__(self, data):
        self.data = data


class Graph:
    def __init__(self, size):
        self.nodes = []
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, src, dst):
        self.matrix[src][dst] = 1
        self.matrix[dst][src] = 1

    def check_edge(self, src, dst):
        return self.matrix[src][dst] == 1

    def print_graph(self):
        print("  ", end="")
        for node in self.nodes:
            print(node.data, end=" ")
        print()

        for i in range(len(self.matrix)):
            print(self.nodes[i].data, end=" ")
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=" ")
            print()


# Main
if __name__ == "__main__":
    # Create a graph with 5 nodes
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
    graph.add_edge(1, 4)  # Line added per the comment
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(4, 0)
    graph.add_edge(4, 2)

    # Print the graph
    graph.print_graph()

    # Check if an edge exists
    # print(graph.check_edge(0, 1))
