
# 73. Write a Python function to implement merge sort.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        """Merge two sorted lists into one sorted list."""
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


arr = [3, 6, 8, 10, 4, 2, 1]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
