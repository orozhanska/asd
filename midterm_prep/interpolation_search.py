def interpolation_search(arr, target):
    """
    Perform interpolation search on a sorted array.

    :param arr: List of sorted elements
    :param target: Value to find
    :return: Index of the target in the array, or -1 if not found
    """
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Prevent division by zero
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            else:
                return -1

        # Calculate the position using the interpolation formula
        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))

        # Check if the target is at the calculated position
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example usage:
array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 40

result = interpolation_search(array, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found.")
