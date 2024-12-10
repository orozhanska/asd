class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        # self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        #child.parent = self
parent_node = Node(1)
child_node = Node(2)
parent_node.children.append(child_node)

# vs 
parent_node.add_child(child_node)

def dfs(visited, tree, node):  #
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in node.children:
            dfs(visited, tree, neighbour)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#dfs with binary - we do not need visited 

def dfs(root): #or node
    if root is None:
        return
    print(root.data)  #pre-order
    # if root.left:
    dfs(root.left)
    # in-order
    # if root.right:
    dfs(root.right)
    #post-order


