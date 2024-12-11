"""
I used Depth First Search to check for cycles. If while traversing through the graph we come back to the node already in our stack - the cycle is detected  
Time complexity is O(n + k) as we iterate first through nodes than traverse through edges

"""

def build_graph(n, edges):
    # in the test cases the sellers are indexed from 0 to n so we can use a simple list representation of a hashtable
    graph = [[] for _ in range(n)] # builds a hashtable to store adjacent nodes 
    for u, v in edges:
        graph[u].append(v) # as the graph is directed
    return graph

def has_cycle(n, edges):
    """
    Detect if there is a cycle in a directed graph using ***(you to choose)  algorithm.

    """
    graph = build_graph(n, edges)
    visited = [False] * n # visited are nodes which do not have adjacent nodes or which have visited adjacent nodes
    rec_stack = [False] * n # track the path we are on

    for i in range(n): # iterate through nodes as the graph is directed and some nodes can be disconnected
        if not visited[i]:
            if dfs(i, graph, visited, rec_stack):
                return True  
    return False  


def dfs(node, graph, visited, rec_stack):
    stack = [node]  
    
    while stack:
        current = stack[-1]  
        if not visited[current]:
            visited[current] = True
            rec_stack[current] = True
            
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                elif rec_stack[neighbor]: # if we traversed through this node with dfs previously and return to it - the cucle is detected
                    return True
        else:
            rec_stack[current] = False
            stack.pop()
    
    return False



def test_supply_cycle_detection():
    """
    Test cases for cycle detection in a supply network.
    """
    # Test 1: Example with a cycle
    n = 4
    edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
    result = has_cycle(n, edges)
    assert result == True, f"Test 1 failed. Expected: True, Got: {result}"

    print("Example Input:")
    print("Cycle Detection: Yes")
    print()

    # Test 2: No cycle
    n = 4
    edges = [(0, 1), (1, 2), (2, 3)]
    result = has_cycle(n, edges)
    assert result == False, f"Test 2 failed. Expected: False, Got: {result}"

    print("Cycle Detection: No")
    print()

    # Test 3: Single node, no cycle
    n = 1
    edges = []
    result = has_cycle(n, edges)
    assert result == False, f"Test 3 failed. Expected: False, Got: {result}"

    # Test 4: Self-loop (cycle)
    n = 3
    edges = [(0, 0), (1, 2)]
    result = has_cycle(n, edges)
    assert result == True, f"Test 4 failed. Expected: True, Got: {result}"

    print("Cycle Detection: Yes (Self-loop)")
    print()

    # Test 5: Multiple disconnected components with one cycle
    n = 5
    edges = [(0, 1), (1, 2), (2, 0), (3, 4)]
    result = has_cycle(n, edges)
    assert result == True, f"Test 5 failed. Expected: True, Got: {result}"

    print("Cycle Detection: Yes (Disconnected components)")
    print()

    print("All tests passed successfully!")

if __name__ == "__main__":
    test_supply_cycle_detection()
