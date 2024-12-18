# Task #4


class MinHeap: # modify to manage tuples (current_distance, node)
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _get_parent(self, index):
        return (index - 1) // 2

    def _heapify_up(self, index):
        parent = self._get_parent(index)
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _get_left_child(self, index):
        return 2 * index + 1

    def _get_right_child(self, index):
        return 2 * index + 2

    def _heapify_down(self, index):
        left = self._get_left_child(index)
        right = self._get_right_child(index)
        smallest = index

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

def dijkstra_heap(graph, start, finish):
    """
    Dijkstra's algorithm using a custom MinHeap.
    :param graph: dict of lists, where graph[u] = [(v, weight), ...]
    :param start_node: starting node
    :param target_node: target node
    :return: (distance, path) to target node
    """
    distances = {node: float('inf') for node in graph}
    prev_node = {node: None for node in graph}
    distances[start] = 0

    heap = MinHeap()
    heap.insert((0, start)) 

    visited = set()

    while len(heap.heap) > 0:
        current_distance, current_node = heap.extract_min()

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == finish:
            break

        for neighbor, weight in list(graph[current_node].items()):
            if neighbor in visited:
                continue

            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                prev_node[neighbor] = current_node
                heap.insert((new_distance, neighbor))


    if distances[finish] == float('inf'):
        path = []
    else: 
        path = []
        current = finish
        while current is not None:
            path.append(current)
            current = prev_node[current]
        path.reverse()

    return distances[finish], path 



# Test case generator
def generate_test_cases():
    test_cases = []

    # Test Case 1: Simple graph
    test_cases.append((
        {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        },
        'A',
        'D',
        (4, ['A', 'B', 'C', 'D'])
    ))

    # Test Case 2: Disconnected graph
    test_cases.append((
        {
            'A': {'B': 1},
            'B': {},
            'C': {'D': 1},
            'D': {}
        },
        'A',
        'D',
        (float('inf'), [])
    ))

    # Test Case 3: Single node graph
    test_cases.append((
        {
            'A': {}
        },
        'A',
        'A',
        (0, ['A'])
    ))

    # Test Case 4: No edges
    test_cases.append((
        {
            'A': {},
            'B': {},
            'C': {}
        },
        'A',
        'C',
        (float('inf'), [])
    ))

    # Test Case 5: Multiple paths
    test_cases.append((
        {
            'A': {'B': 1, 'C': 5},
            'B': {'C': 2, 'D': 4},
            'C': {'D': 1},
            'D': {}
        },
        'A',
        'D',
        (4, ['A', 'B', 'C', 'D'])
    ))

    # Test Case 6: Larger graph
    test_cases.append((
        {
            'A': {'B': 2, 'C': 5},
            'B': {'C': 1, 'D': 4, 'E': 7},
            'C': {'D': 1},
            'D': {'E': 3},
            'E': {'F': 2},
            'F': {}
        },
        'A',
        'F',
        (9, ['A', 'B', 'C', 'D', 'E', 'F'])
    ))

    # Test Case 7: Cyclic graph
    test_cases.append((
        {
            'A': {'B': 1},
            'B': {'C': 2},
            'C': {'A': 3, 'D': 1},
            'D': {}
        },
        'A',
        'D',
        (4, ['A', 'B', 'C', 'D'])
    ))

    # Test Case 8: Dense graph
    test_cases.append((
        {
            'A': {'B': 1, 'C': 2, 'D': 3},
            'B': {'C': 1, 'D': 2, 'E': 4},
            'C': {'D': 1, 'E': 3},
            'D': {'E': 1},
            'E': {}
        },
        'A',
        'E',
        (4, ['A', 'D', 'E'])
    ))

    # Test Case 9: Long chain graph
    test_cases.append((
        {
            'A': {'B': 1},
            'B': {'C': 1},
            'C': {'D': 1},
            'D': {'E': 1},
            'E': {'F': 1},
            'F': {}
        },
        'A',
        'F',
        (5, ['A', 'B', 'C', 'D', 'E', 'F'])
    ))

    return test_cases


def path_is_valid(graph, path, start, finish, distance):
    if not path:
        return distance == float('inf')
    if path[0] != start or path[-1] != finish:
        return False
    for i in range(len(path) - 1):
        if path[i + 1] not in graph[path[i]]:
            return False
    # check distances
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance == distance


# Run tests
def run_tests():
    test_cases = generate_test_cases()

    for i, (graph, start, finish, expected) in enumerate(test_cases):
        distance, path = dijkstra_heap(graph, start, finish)
        assert distance == expected[0], f"Test case {i + 1} failed: {distance} != {expected[0]}"
        assert path_is_valid(graph, path, start, finish,
                             distance), f"Test case {i + 1} failed: {path} is not a valid path"
        # Note: there can be a couple of valid paths, so we only check if the path is valid
        # you can comment if needed, but not path_is_valid() call
        assert path == expected[1], f"Test case {i + 1} failed: {path} != {expected[1]}"

    print("All test cases passed!")


# Run the test suite
run_tests()
