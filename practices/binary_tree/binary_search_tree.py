class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _search(self, root, value):
        if root is None:
            return False
        
        if root.data == value:
            return True
        
        if value < root.data:
            return self._search(root.left, value)
        return self._search(root.right, value)
        
    def search(self, value) :
        return self._search(self.root, value)
    
    def _insert(self, root, value):
        if root is None:
            return BinaryTreeNode(value)
        
        if root.data == value:
            return root
        
        if value < root.data:
            root.left = self._insert(root.left, value)
        
        else:
            root.right = self._insert(root.right, value)
        
        return root
        
        

    def insert(self, value):
        self.root = self._insert(self.root,value)

    def _remove(self, root, value):
        if root is None:
            return None  # Correctly handle None case

        if root.data == value:
            # 1. Leaf node
            if root.left is None and root.right is None:
                return None
            
            # 2. Node with one child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # 3. Node with two children
            # Find max in left subtree
            max_left = root.left
            while max_left.right:
                max_left = max_left.right
            root.data = max_left.data
            root.left = self._remove(root.left, max_left.data)

        elif value < root.data:
            root.left = self._remove(root.left, value)
        else:
            root.right = self._remove(root.right, value)

        return root



    def remove(self, value):
        self.root = self._remove(self.root, value)
    
    def _print_sorted(self, root):
        if root is None:
            return
        
        self._print_sorted(root.left)
        print(root.data)
        self._print_sorted(root.right)
    
    def print_sorted(self):
        self._print_sorted(self.root)

    
        


bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)

print(bst.search(8))
print(bst.search(7))

bst.remove(1)
print(bst.search(1))

bst.print_sorted()