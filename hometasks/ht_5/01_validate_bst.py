#### Task 1: Validating a Binary Search Tree
# Write a function to validate whether a given binary tree is a valid Binary Search Tree (BST). 
# A valid BST satisfies the following conditions:
# 1. The left subtree of a node contains only nodes with values less or equal than the node’s value.
# 2. The right subtree of a node contains only nodes with values greater than the node’s value.
# 3. Both left and right subtrees must also be valid BSTs.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(root):
    return node_valid(root, float('inf'), float('-inf'))


def node_valid(root, highest, lowest):

    if not root:
        return True
    
    if not lowest < root.value < highest:
        return False 

    return node_valid(root.left, root.value, lowest) and node_valid(root.right, highest, root.value)
        



# Example test cases
#        10
#       /  \
#      5   15
#     / \  / \
#    2  7 12 20
def Test1():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    assert is_valid_bst(root) is True


# Invalid BST example
#        10
#       /  \
#      5   15
#     / \
#    2  12
def Test2():
    root_invalid = TreeNode(10)
    root_invalid.left = TreeNode(5)
    root_invalid.right = TreeNode(15)
    root_invalid.left.left = TreeNode(2)
    root_invalid.left.right = TreeNode(12)  # This makes it invalid
    assert is_valid_bst(root_invalid) is False


# Single node tree
def Test3():
    root = TreeNode(-5)
    assert is_valid_bst(root) is True


# Valid BST example
#        10
#       /  \
#      5   15
#     / \  / \
#    2  7 12 20
#              \
#               25
#                \
#                 30
def Test4():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    root.right.right.right = TreeNode(25)
    root.right.right.right.right = TreeNode(30)

    assert is_valid_bst(root) is True


Test1()
Test2()
Test3()
Test4()
print("All test cases pass")
