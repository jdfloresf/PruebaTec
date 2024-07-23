# 71. Write a Python function to implement binary search.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target is not present in the array
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print(f"Element {target} is not present in the array")
