def create_graph(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def greedy_coloring(n, edges):
    graph = create_graph(n, edges)
    colors = [-1] * (n + 1)

    for node in range(1, n + 1):
        # TODO: Find colors of all neighbors
        neighbor_colors = {...}  # Fill this part

        # TODO: Assign the smallest available color
        color = 1
        while ...:
          pass

    return colors[1:], max(colors)

