"""
Floyd-Warshall algorithm is used as it allows to count shortest paths between each of the two nodes - cities in our case
Time complexity is O(n^3) as we have 3 loops
Space complexity in O(n^2) as we save the data in the two-dimensional arrays

"""
import math

INF = "INF"


def foo(n, roads):
    """
     algorithm to calculate the shortest travel times between all pairs of cities.
    """
    # why foo ...

    # if the cities are not represented as indices but as Letters A, B, C ot maybe names like Kyiv
    # create a mapping
    # this works only if roads contain all cities
    # list1 = [road[1] for road in roads
    # city_names = [road[0] for road in roads]
    # city_names.extend(list1)
    # city_names = list(set(city_names))

    # mapping_nametoind = {name: ind for ind, name in enumerate(city_names)}
    # mapping_indtoname = {ind: name for ind, name in enumerate(city_names)}


    shortest_path = [[float('inf')]*n for _ in range(n)]
    next_hop = [[None]*n for _ in range(n)]

    for i in range(n):
        shortest_path[i][i] = 0

    for c_1, c_2, duration in roads:
        shortest_path[c_1][c_2] = duration
        shortest_path[c_2][c_1] = duration
        next_hop[c_1][c_2] = c_2
        next_hop[c_2][c_1] = c_1

    # Floyd Warshall Algorithm for counting the shortest paths between each of the two cities

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if shortest_path[i][j] > (shortest_path[i][k]+shortest_path[k][j]):
                    shortest_path[i][j] = shortest_path[i][k]+shortest_path[k][j]
                    next_hop[i][j] = next_hop[i][k]
    
    for i in range(n):
        for j in range(n):
            if shortest_path[i][j] == float('inf'):
                shortest_path[i][j] = INF
    
    return shortest_path, next_hop

"""
When adding a road (a, b, duration) we need to reclculate the shortest path between each city i and j
We iterate two times (O(n^2)) and check if the shortest path changes if we go from i -> a -> b -> j
shortest_path[i][j] = min(
    shortest_path[i][j],
    shortest_path[i][a] + duration + shortest_path[b][j]
)
We apdate next_hop as well accordingly

When removing  road from a to b, we set the shortest path from a to b as INF and recalculate  
the paths from the scratch.

"""



def reconstruct_path(next_hop, start, end):
    """
    Reconstruct the shortest path using the next_hop matrix.
    """
    if next_hop[start][end] is None:
        return None
    
    path = [start]
    while start != end:
        start = next_hop[start][end]
        path.append(start)
    
    return path



def test_transportation_network():
    """
    Test cases for the transportation network optimization.
    """
    # Test 1: Example case
    n = 5
    roads = [
        (0, 1, 4),
        (0, 2, 6),
        (0, 3, 7),
        (0, 4, 10),
        (1, 2, 2),
        (1, 3, 3),
        (1, 4, 6),
        (2, 3, 1),
        (2, 4, 4),
        (3, 4, 3)
    ]
    dist, next_hop = foo(n, roads)

    expected_matrix = [
        [0, 4, 6, 7, 10],
        [4, 0, 2, 3, 6],
        [6, 2, 0, 1, 4],
        [7, 3, 1, 0, 3],
        [10, 6, 4, 3, 0]
    ]

    assert dist == expected_matrix, f"Test 1 failed. Got:\n{dist}"

    # Test 2: Disconnected cities
    n = 3
    roads = [(0, 1, 5)]
    dist, next_hop = foo(n, roads)

    expected_matrix = [
        [0, 5, INF],
        [5, 0, INF],
        [INF, INF, 0]
    ]

    assert dist == expected_matrix, f"Test 2 failed. Got:\n{dist}"

    # Test 3: Single city
    n = 1
    roads = []
    dist, next_hop = foo(n, roads)

    expected_matrix = [[0]]
    assert dist == expected_matrix, f"Test 3 failed. Got:\n{dist}"

    # Test 4: Dynamic update - Adding a road
    n = 4
    roads = [
        (0, 1, 3),
        (1, 2, 1)
    ]
    dist, next_hop = foo(n, roads)

    # Add a new road dynamically
    roads.append((2, 3, 2))
    dist, next_hop = foo(n, roads)

    expected_matrix = [
        [0, 3, 4, 6],
        [3, 0, 1, 3],
        [4, 1, 0, 2],
        [6, 3, 2, 0]
    ]

    assert dist == expected_matrix, f"Test 4 failed. Got:\n{dist}"

    # Test 5: Dynamic update - Removing a road
    roads.remove((1, 2, 1))
    dist, next_hop = foo(n, roads)

    expected_matrix = [
        [0, 3, INF, INF],
        [3, 0, INF, INF],
        [INF, INF, 0, 2],
        [INF, INF, 2, 0]
    ]

    assert dist == expected_matrix, f"Test 5 failed. Got:\n{dist}"

    print("All tests passed successfully!")


if __name__ == "__main__":
    test_transportation_network()


