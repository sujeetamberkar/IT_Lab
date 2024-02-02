def binary_search_recursive(arr, target, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)
        else:
            return binary_search_recursive(arr, target, mid + 1, high)
    
    else:
        return -1

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 5
result = binary_search_recursive(sorted_array, target_value, 0, len(sorted_array) - 1)
print("Target found at index:", result)
