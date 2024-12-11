# social_group_coloring_tests.py

def create_graph(n, edges):
    graph = {i: [] for i in range(0, n)} # changed from (1, n+1) ro (0,n) as peope are 
    # indexed starting from 0 in the test cases 
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def greedy_coloring(n, edges):
    graph = create_graph(n, edges)
    colors = [-1] * n # changed from (n+1) to n as the people 
    # are matched starting from 0 in test cases
    # [p0 p1 p2 p3] n = 4

    sorted_nodes=sorted(graph.keys(), key=lambda x:len(graph[x]), reverse = True)

    for node in sorted_nodes:
        # Find colors of all neighbors
        neighbor_colors = {colors[adj] for adj in graph[node] if colors[adj]!= -1}  

        # Assign the smallest available color
        color = 1
        while color in neighbor_colors:
            color += 1
        colors[node] = color

    return colors, max(colors) # changed colors[1:] to colors as to match the people indexing from 0




def test_social_group_coloring():
    """
    Test cases for social group coloring.
    """
    # Test 1: Example graph
    n = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    color_assignment, total_colors = greedy_coloring(n, edges)

    print("Test 1 - Example Graph")
    print("Color Assignment:", color_assignment)
    print("Total Colors Used:", total_colors)
    assert total_colors == 2, f"Test 1 failed. Expected 2 colors, got {total_colors}."

    # Test 2: No edges (independent nodes)
    n = 3
    edges = []
    color_assignment, total_colors = greedy_coloring(n, edges)

    print("Test 2 - No Edges")
    print("Color Assignment:", color_assignment)
    print("Total Colors Used:", total_colors)
    assert total_colors == 1, f"Test 2 failed. Expected 1 color, got {total_colors}."

    # Test 3: Complete graph
    n = 4
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    color_assignment, total_colors = greedy_coloring(n, edges)

    print("Test 3 - Complete Graph")
    print("Color Assignment:", color_assignment)
    print("Total Colors Used:", total_colors)
    assert total_colors == 4, f"Test 3 failed. Expected 4 colors, got {total_colors}."

    # Test 4: Bipartite graph
    n = 6
    edges = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
    color_assignment, total_colors = greedy_coloring(n, edges)

    print("Test 4 - Bipartite Graph")
    print("Color Assignment:", color_assignment)
    print("Total Colors Used:", total_colors)
    assert total_colors == 2, f"Test 4 failed. Expected 2 colors, got {total_colors}."

    # Test 5: Disconnected graph
    n = 5
    edges = [(0, 1), (1, 2), (3, 4)]
    color_assignment, total_colors = greedy_coloring(n, edges)

    print("Test 5 - Disconnected Graph")
    print("Color Assignment:", color_assignment)
    print("Total Colors Used:", total_colors)
    assert total_colors == 2, f"Test 5 failed. Expected 2 colors, got {total_colors}."

    print("All tests passed successfully!")


if __name__ == "__main__":
    test_social_group_coloring()
