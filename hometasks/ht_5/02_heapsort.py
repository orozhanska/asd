# Task 2: Heapsort
# You need to implement the heapsort algorithm. For that you need to finish the implementation of the MinHeap class.
# After that, you need to implement the heapsort function that will sort an array using the MinHeap class.
#
# TODO:
# 1. Implement the heapify_up function
# 2. Implement the heapify_down function
# 3. Implement the heapsort function
"""
- Is heapsort is stable sorting algorithm or not? 
Heapsort cannot guarantee stability as the elements are constantly swapped.

- What is the space complexity (in big-O notation) for HeapSort? 
For my solution, space complexity is O(n) as I created an array of MinHeap & additional array sorted_array for sorting.

- Does it have the same time complexity on an almost sorted/sorted arrays?
Yes, the time complexity O(n * logn ) is the same for sorted/not sorted arrays. 
The best case happens when all the values in the array are the same - then the heapifying & removing max value will take O(n)

"""

import random


def random_array(size, lower_bound=-1000, upper_bound=1000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


class MinHeap:
    def __init__(self):
        # We will use a list to store the heap instead of a tree, since our heap is a complete binary tree
        self.heap = []

    def insert(self, value):
        # Insert the value at the end of the heap
        self.heap.append(value)
        # And now we need to heapify that value up to its correct position
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

    # Heapify up - move the value up to its correct position (used when inserting a new value)
    # TODO: Implement the heapify up function
    def _heapify_up(self, index):
        parent = self._get_parent(index)

        if parent >= 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)


    def _get_left_child(self, index):
        return 2 * index + 1

    def _get_right_child(self, index):
        return 2 * index + 2

    # Heapify down - move the value down to its correct position (used when extracting the min)
    # TODO: Implement the heapify down function
    def _heapify_down(self, index):
        left = self._get_left_child(index)
        right = self._get_right_child(index)
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)



# TODO: Implement the heapsort function
def heapsort(arr):
    heap = MinHeap()
    for el in arr:
        heap.insert(el)
    
    sorted_array = []
    while len(heap.heap) > 0:
        sorted_array.append(heap.extract_min())
    return sorted_array


def basic_test(sorting_func):
    arr = [5, 4, 3, 2, 1]
    arr_my = sorting_func(arr)
    res = sorted(arr)
    assert arr_my == res, f"Expected {res}, but my sort got {arr_my}"
    print("\033[92mBasic test passed\033[0m")


def random_test(sorting_func):
    arr = random_array(5)
    print("Random array: ", arr)
    arr_my = sorting_func(arr)
    print("Sorted array: ", arr_my)
    res = sorted(arr)
    assert arr_my == res, f"Expected {res}, but my sort got {arr_my}"
    print("\033[92mRandom test passed\033[0m")


def medium_test(sorting_func):
    arr = random_array(500)
    arr_my = sorting_func(arr)
    res = sorted(arr)
    assert arr_my == res, f"Expected {res}, but my sort got {arr_my}"
    print("\033[92mMedium test passed\033[0m")


def big_test(sorting_func):
    arr = random_array(10000)
    arr_copy = arr.copy()

    import time
    start = time.time()
    arr_my = sorting_func(arr)
    end = time.time()
    print(f"Time to sort 10,000 elements: {end - start:.6f} seconds")

    start = time.time()
    arr_copy.sort()
    end = time.time()
    print(f"Time to sort 10,000 elements with built-in sort: {end - start:.6f} seconds")

    assert arr_my == arr_copy, f"Expected {arr_copy}, but my sort got {arr_my}"
    print("\033[92mBig test passed\033[0m")


if __name__ == "__main__":
    sorting_func = heapsort
    basic_test(sorting_func)
    random_test(sorting_func)
    medium_test(sorting_func)
    big_test(sorting_func)
