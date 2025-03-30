def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Found at index i
    return -1  # Not found

arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))  # Output: 2
