import random
import time


def generate_sorted_array(size, lower_bound=1, upper_bound=10000):
    array = [random.randint(lower_bound, upper_bound) for _ in range(size)]
    return sorted(array)


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary_search(arr, x):
    low_ind, high_ind = 0, len(arr) - 1
    while low_ind <= high_ind:
        mid = low_ind + (high_ind - low_ind) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high_ind = mid - 1
        else:
            low_ind = mid + 1

    return -1

sizes = [1000, 10000, 100000, 1000000]
results = {}

for size in sizes:
    array = generate_sorted_array(size)
    target = array[-1]

    start_time = time.time()
    linear_search(array, target)
    linear_time = time.time() - start_time

    start_time = time.time()
    binary_search(array, target)
    binary_time = time.time() - start_time

    results[size] = {'linear_search': linear_time, 'binary_search': binary_time}

for size, times in results.items():
    print(f"Array Size: {size}")
    print(f"Linear Search Time: {times['linear_search']} seconds")
    print(f"Binary Search Time: {times['binary_search']} seconds")
    print()