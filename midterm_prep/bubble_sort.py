def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.

    :param arr: List of elements to sort
    :return: Sorted array (in-place)
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize and stop early if no swaps are made
        swapped = False
        for j in range(n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps are made, the array is sorted
        if not swapped:
            break

# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", array)

bubble_sort(array)
print("Sorted array:", array)
