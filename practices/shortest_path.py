graph = {
    1: [(3, 9), (2, 7), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(3, 2), (5, 9), (1, 14)],
}
start_node = 1

distances = {node: float('inf') for node in graph}
prev_node = {node: None for node in graph}
distances[start_node] = 0
prev_node[start_node] = start_node

#prev_node[5] -> (x-> 5)

visited = set() # or [] or {}

# Heap 
# Priority queue
# O(log N)

num_of_nodes = len(graph)

for iteration in range(num_of_nodes):
    min_distance = float('inf')
    min_node = None

    for node in graph:
        if node in visited:
            continue
        if distances[node] < min_distance:
            min_distance = distances[node]
            min_node = node
    # min_node should not be none
    for edge in graph[min_node]:
        to_node, weight = edge
        # distances[to_node] = min(distances[to_node], 
        #                          distances[min_node]+weight)
        
        if distances[min_node] + weight < distances[to_node]:
            distances[to_node] = distances[min_node] + weight
            prev_node[to_node] = min_node

    visited.add(min_node)


print(distances)
print(prev_node)

finish_node = 5
path = []
while finish_node != start_node:
    path.append(finish_node)
    finish_node = prev_node[finish_node]
path.append(start_node)
print(path[::-1])


# (from, to, weight)
# list_of_edges = [ 
#    (1,2,9),
#    ..

# # ]
# graph = {}

# for edge in list_of_edges:
#     from_node, to_node, weight = edge
#     if from_node not in graph:
#         graph[from_node] = []
#     graph[from_node].append((to_node, weight))

#     if to_node not in graph:
#         graph[to_node] = []
#     graph[to_node].append((from_node, weight))