# rearrange arrows 
# elements <= pivot, pivot, elements >= pivot
def partition(arr, left, right, pivot):
    # [5, 4, 1, 3, 7], pivot = 5
    # after: [4, 1, 3] 5 [7]
    smaller = []
    larger = []
    pivot_count = 0  

    for i in range(left, right + 1):
        if arr[i] < pivot:
            smaller.append(arr[i])
        elif arr[i] == pivot:
            pivot_count += 1
        else:
            larger.append(arr[i])

    arr[left:(right + 1)] = smaller + [pivot] * pivot_count + larger
    pivot_index = left + len(smaller)
    return pivot_index


def quick_sort(arr, left, right):
    if left >= right:
        return 
    
    pivot = arr[right]
    index = partition(arr, left, right, pivot)

    quick_sort(arr, left, index - 1)
    quick_sort(arr, index + 1, right)


# the tests are by chatgpt

def test_partition():
    # Test 1: Basic test with distinct numbers
    arr = [5, 4, 1, 3, 7]
    pivot_index = partition(arr, 0, len(arr) - 1, 5)
    assert arr == [4, 1, 3, 5, 7], f"Failed Test 1, got {arr}"
    assert pivot_index == 3, f"Failed Test 1 Pivot Index, got {pivot_index}"

    # Test 2: Already sorted array
    arr = [1, 2, 3, 4, 5]
    pivot_index = partition(arr, 0, len(arr) - 1, 3)
    assert arr == [1, 2, 3, 4, 5], f"Failed Test 2, got {arr}"
    assert pivot_index == 2, f"Failed Test 2 Pivot Index, got {pivot_index}"

    # Test 3: Reverse sorted array
    arr = [5, 4, 3, 2, 1]
    pivot_index = partition(arr, 0, len(arr) - 1, 3)
    assert arr == [2, 1, 3, 5, 4], f"Failed Test 3, got {arr}"
    assert pivot_index == 2, f"Failed Test 3 Pivot Index, got {pivot_index}"

    # Test 4: Array with duplicates
    arr = [4, 5, 3, 4, 1]
    pivot_index = partition(arr, 0, len(arr) - 1, 4)
    assert pivot_index == 2, f"Failed Test 4 Pivot Index, got {pivot_index}"

    # Test 5: Single-element array
    arr = [5]
    pivot_index = partition(arr, 0, 0, 5)
    assert arr == [5], f"Failed Test 5, got {arr}"
    assert pivot_index == 0, f"Failed Test 5 Pivot Index, got {pivot_index}"

    # Test 6: Empty array
    arr = []
    try:
        partition(arr, 0, 0, 5)
        assert False, "Failed Test 6: Expected IndexError"
    except IndexError:
        pass  # Expected behavior


def test_quick_sort():
    # Test 1: Basic test with distinct numbers
    arr = [5, 4, 1, 3, 7]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 3, 4, 5, 7], f"Failed Test 1, got {arr}"

    # Test 2: Already sorted array
    arr = [1, 2, 3, 4, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5], f"Failed Test 2, got {arr}"

    # Test 3: Reverse sorted array
    arr = [5, 4, 3, 2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5], f"Failed Test 3, got {arr}"

    # Test 4: Array with duplicates
    arr = [4, 5, 3, 4, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 3, 4, 4, 5], f"Failed Test 4, got {arr}"

    # Test 5: Single-element array
    arr = [5]
    quick_sort(arr, 0, 0)
    assert arr == [5], f"Failed Test 5, got {arr}"

    # Test 6: Empty array
    arr = []
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [], f"Failed Test 6, got {arr}"

    # Test 7: Large array
    arr = [10, -1, 2, 8, 7, 3, 5, 4, 6, 9]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr), f"Failed Test 7, got {arr}"


if __name__ == "__main__":
    test_partition()
    print("All partition tests passed.")
    test_quick_sort()
    print("All quick_sort tests passed.")


    
