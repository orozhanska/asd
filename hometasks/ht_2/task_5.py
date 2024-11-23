# Task 5: Top-K Frequent Elements
# Score: 3 points

# ● Write a function to find the top K most frequent elements in an array.
# ● Array can be unsorted.
# ● Elements are in the range [1, 1000].
# ● K is in the range [1, 1000].
# ● If there are multiple elements with the same frequency, return any of them.
# ○ For example, [1, 1, 1, 2, 2, 2], k = 1 can return either 1 or 2.
# ● Example 1: [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2]
# ○ Explanation: 1 is repeated 3 times, 2 is repeated 2 times, and 3 is repeated 1
# time. So, the top 2 frequent elements are 1 and 2.
# ● Example 2: [2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 6], k = 3 -> [2, 3, 4]
# ○ Explanation: 2, 3, and 4 are repeated 3 times, and 5 is repeated 2 times. So,
# the top 3 frequent elements are 2, 3, and 4.
# ● It’s not allowed to use a built-in dictionary or set data structures from Python. As well
# as additional libraries (except the basic ones like random, and time).
# ○ but it’s allowed to use built-in sort from Python.
# ● Explain the time & space complexity of your algorithm.

#lets reuse the third task


# def most_frequent(arr, k):
#     arr = sorted(arr)
#     repetitions = []
#     count = 1
#     temp_tuple = None
#     for x in range(len(arr)-1):
#         if arr[x+1] == arr[x]:
#             count += 1
#             temp_tuple = (arr[x], count)
#         else:
#             if temp_tuple:
#                 repetitions.append(temp_tuple)
#             count = 1
#             temp_tuple = None
    
    
#     if temp_tuple:
#         repetitions.append(temp_tuple)
    
#     for x in arr:
#         if x not in [x[0] for x in repetitions]:
#             repetitions.append((x, 1))

#     repetitions = sorted(repetitions, key=lambda t: t[1], reverse=True)
#     most = [x[0] for x in repetitions[:k]] if k < len(repetitions) else [x[0] for x in repetitions]
#     return most

# or lets just not use the previous task

def most_frequent(arr, k):
    repetitions = []
    current = arr[0]
    count = 1

    for i in range(1, len(arr)):  
        if arr[i] == current:
            count += 1
        else:
            repetitions.append((current, count))
            current = arr[i]
            count = 1
    
    repetitions.append((current, count))

    repetitions = sorted(repetitions, key=lambda t: t[1], reverse=True) 
    print(repetitions)
    most = [x[0] for x in repetitions[:k]] if k < len(repetitions) else [x[0] for x in repetitions]
    return most



print(most_frequent([1, 1, 1, 2, 2, 3], 2))
print(most_frequent([2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 6], 3))
print(most_frequent([10, 10, 20, 20, 20, 30], 1))

#tests by chatgpt

import unittest

class TestMostFrequent(unittest.TestCase):

    def test_basic_case(self):
        arr = [1, 1, 1, 2, 2, 3]
        k = 2
        result = most_frequent(arr, k)
        self.assertCountEqual(result, [1, 2])

    def test_multiple_same_frequencies(self):
        arr = [2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 6]
        k = 3
        result = most_frequent(arr, k)
        self.assertCountEqual(result, [2, 3, 4])  # Any order is acceptable

    def test_single_element(self):
        arr = [1]
        k = 1
        result = most_frequent(arr, k)
        self.assertEqual(result, [1])


    def test_all_elements_same(self):
        arr = [7, 7, 7, 7]
        k = 1
        result = most_frequent(arr, k)
        self.assertEqual(result, [7])

    def test_partial_k(self):
        arr = [1, 2, 2, 3, 3, 3]
        k = 1
        result = most_frequent(arr, k)
        self.assertEqual(result, [3])

    def test_larger_k_than_unique_elements(self):
        arr = [1, 1, 2, 2, 3]
        k = 4  # Only 3 unique elements
        result = most_frequent(arr, k)
        self.assertCountEqual(result, [1, 2, 3])  # Returns all unique elements

    def test_unsorted_array(self):
        arr = [4, 5, 6, 4, 6, 5, 5]
        k = 2
        result = most_frequent(arr, k)
        self.assertCountEqual(result, [5, 4])  # 5 occurs 3 times, 4 occurs 2 times

    def test_k_equals_unique_count(self):
        arr = [8, 7, 8, 9, 7, 9, 9]
        k = 3
        result = most_frequent(arr, k)
        self.assertCountEqual(result, [7, 8, 9])  # All 3 unique elements are included

    def test_k_is_one(self):
        arr = [10, 10, 20, 20, 20, 30]
        k = 1
        result = most_frequent(arr, k)
        self.assertEqual(result, [20])  # 20 occurs most frequently

if __name__ == '__main__':
    unittest.main()

