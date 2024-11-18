def merge(left, right):
    n_1 = len(left) 
    n_2 = len(right) 
    res = []
    i = 0 # start of right
    j = 0 # start of left

    while i < n_1 and j < n_2:
        if left[i] < right[j]: #compare the smallest numbers in the lists
            res.append(left[i])  # the smallest in two arrays
            i += 1 # no meaning to compare to the smallest again. lets find the next smallest
        
        else: # compare the smallest numbers in the list -> we get that the right first is smaller
            res.append(right[j]) # the smallest in arrays is found
            j += 1 # go to the next in arrow 2
        
    while i < n_1:
        res.append(left[i])
        i+=1
    
    while j < n_2:
        res.append(right[j])
        j+=1
    
    return res

def merge_sort (array):
    if len(array) <= 1: # if we decomposited to the full
        return array 
    
    mid = len(array) // 2 # divide

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge (left, right)

print(merge_sort([1,5,3,19,45,3,5,6]))

# chatGPT next (but they are alays here anyways)
def test_merge_sort():
    # Standard case
    assert merge_sort([1, 5, 3, 19, 45, 3, 5, 6]) == [1, 3, 3, 5, 5, 6, 19, 45]
    
    # Already sorted
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Reverse order
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Single element
    assert merge_sort([42]) == [42]

    # Empty list
    assert merge_sort([]) == []

    # Duplicates
    assert merge_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]

    # Negative numbers
    assert merge_sort([-1, -3, -2, -5, -4]) == [-5, -4, -3, -2, -1]

    # Mixed positive and negative
    assert merge_sort([-1, 3, -2, 5, 0]) == [-2, -1, 0, 3, 5]

    # Large numbers
    assert merge_sort([1000000, 500000, 2000000]) == [500000, 1000000, 2000000]

    # Floating point numbers
    assert merge_sort([1.1, 0.5, 2.3, 1.2]) == [0.5, 1.1, 1.2, 2.3]

    print("All tests passed!")
    
# Run the tests
test_merge_sort()


