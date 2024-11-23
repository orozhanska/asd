# I am sorry, I didn't notice the zip files with tests and I generated some with chatgpt
# Write a function to check if an array is sorted in non-ascending or non-descending
# order or not sorted at all.
# ● Return -1 if the array is sorted in non-ascending order, 
# ● 1 if it is sorted in non-descending order, 
# ● and 0 if it is not sorted at all.
# ● If the array is sorted in both non-ascending and non-descending order, 
# return 2.

def is_sorted(arr):
    if len(set(arr)) <= 1:
        return 2
    
    is_non_descnending = []
    is_non_ascending = []

    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]: # check for ascending
            is_non_descnending.append(True)
            is_non_ascending.append(False)
        elif arr[i] > arr[i + 1]:
            is_non_descnending.append(False)
            is_non_ascending.append(True)
            
    
    if all(is_non_descnending):
        return 1
    elif all(is_non_ascending):
        return -1
    return 0

def test_check_sorted():
    assert is_sorted([1, 2, 3, 4, 5]) == 1, "Test Case 1 Failed"
    assert is_sorted([5, 4, 4, 2, 1]) == -1, "Test Case 2 Failed"
    assert is_sorted([1, 1, 1, 1]) == 2, "Test Case 3 Failed"
    assert is_sorted([3, 1, 4, 2]) == 0, "Test Case 4 Failed"
    assert is_sorted([]) == 2, "Test Case 5 Failed"
    assert is_sorted([42]) == 2, "Test Case 6 Failed"
    assert is_sorted([1, 3, 2]) == 0, "Test Case 7 Failed"
    assert is_sorted([10, 9, 8, 8, 7]) == -1, "Test Case 8 Failed"
    assert is_sorted([7, 7, 8, 9, 10]) == 1, "Test Case 9 Failed"
    assert is_sorted([5, 5, 5, 5, 5]) == 2, "Test Case 10 Failed"
    print("All test cases passed!")

test_check_sorted()
