class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        largest = index

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def remove_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def __str__(self):
        return str(self.heap)

# Example usage
heap = MaxHeap()

# Insert values
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(15)
print("Heap after inserts:", heap)

# Check max
print("Max value:", heap.get_max())

# Remove max
removed_max = heap.remove_max()
print("Removed max:", removed_max)
print("Heap after removing max:", heap)
