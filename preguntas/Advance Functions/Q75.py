# 75. Write a Python function to implement selection sort.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        # Iterate over the unsorted subarray to find the actual minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted subarray
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
