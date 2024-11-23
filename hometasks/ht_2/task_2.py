# Task 2: Merge Sort & Insertion Sort + Comparison
# Score: 2 points (0.75pt per each algorithm + 0.5pt for comparison)
# 1. Implement Merge Sort and Insertion Sort.
# 2. Compare them based on:
# ○ Time and space complexities.
# ○ Stability.
# ○ Performance on sorted or almost sorted arrays.
import random


def random_array(size, lower_bound=-1000, upper_bound=1000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


def merge_sort(array):
    if len(array) <= 1:  
        return array
    
    mid = len(array) // 2 
    left = array[:mid]
    right = array[mid:]


    merge_sort(left)
    merge_sort(right)

    merge_into(array, left, right)


def merge_into(array, left, right):
    i = j = k = 0  

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i + 1
        while(j > 0):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j = j-1
            else:
                break
    return arr

def basic_test(sorting_func):
    arr = [5, 4, 3, 2, 1]
    sorting_func(arr)
    assert arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mBasic test passed\033[0m")


def random_test(sorting_func):
    arr = random_array(5)
    print("Random array: ", arr)
    sorting_func(arr)
    print("Sorted array: ", arr)
    assert arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mRandom test passed\033[0m")


def medium_test(sorting_func):
    arr = random_array(500)
    sorting_func(arr)
    assert arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mMedium test passed\033[0m")


def big_test(sorting_func):
    arr = random_array(10000)
    arr_copy = arr.copy()

    import time
    start = time.time()
    sorting_func(arr)
    end = time.time()
    print(f"Time to sort 10,000 elements: {end - start:.6f} seconds")

    start = time.time()
    arr_copy.sort()
    end = time.time()
    print(f"Time to sort 10,000 elements with built-in sort: {end - start:.6f} seconds")

    assert arr == arr_copy, f"Expected {arr_copy}, but my sort got {arr}"
    print("\033[92mBig test passed\033[0m")


if __name__ == "__main__":
    sorting_func = merge_sort
    print("Merge sort")
    basic_test(sorting_func)
    random_test(sorting_func)
    medium_test(sorting_func)
    big_test(sorting_func)

    sorting_func = insertion_sort
    print("\nInsertion sort")
    basic_test(sorting_func)
    random_test(sorting_func)
    medium_test(sorting_func)
    big_test(sorting_func)

# 2. Compare them based on:
# ○ Time and space complexities.
# Time
# -merge sort: O(n*logn) for all cases
# - insertion sort: O(n^2) on average and O(n) in the best case
# Space
# - merge sort: O(n)
# - insertion sort: O(1) - in-place algorithm 

# ○ Stability.
# - both merge andinsertion sort are stable

# ○ Performance on sorted or almost sorted arrays.
# - insertion sort is highly efficient for sorted or almost sorted arrays, 
# where it performs O(n)
# - the merge sort always has a complexiy of O(n*logn)