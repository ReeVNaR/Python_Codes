def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid  # Found
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 30))  # Output: 2
