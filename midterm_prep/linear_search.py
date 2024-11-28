def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return None


print(linear_search([1,2,3,4], 5))