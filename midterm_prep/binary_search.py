arr = [n for n in range(1000)]
target = 42


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (high + low) // 2
        print("middle: ", middle)
        value = arr[middle]

        if value < target:
            low = middle + 1

        elif value > target:
            high = middle - 1

        else:
            return middle

    return -1


print(binary_search(arr, target))
