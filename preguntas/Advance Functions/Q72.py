# 72. Write a Python function to implement quicksort.

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


arr = [3, 6, 8, 10, 4, 2, 1]
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
