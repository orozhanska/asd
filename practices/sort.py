import random


def random_array(size):
    return [random.randint(-100, 100) for _ in range(size)]


def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_ind = i
        for k in range (i, len(arr)):
            if arr[k] < arr[min_ind]:
                min_ind = k
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i + 1
        while(j > 0):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j = j - 1
            else:
                break
    return arr

def reverse_sort(arr):
    for i in range(0, len(arr)-1):
        max_ind = i
        for k in range (i, len(arr)):
            if arr[k] > arr[min_ind]:
                min_ind = k
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
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


sorting_func = selection_sort
print("Selection sort")
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
