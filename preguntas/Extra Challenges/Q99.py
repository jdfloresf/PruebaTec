# 99. Write a Python program to find the maximum sum subarray 
# using Kadane's algorithm.

def max_sum_subarray(arr):
    """
    Find the maximum sum subarray using Kadane's algorithm.

    Parameters:
    arr (list of int): The input array of integers.

    Returns:
    int: The maximum sum of the subarray.
    """
    if not arr:
        return 0

    # Initialize variables
    max_current = max_global = arr[0]

    # Iterate through the array
    for num in arr[1:]:
        # Update max_current to be either the current element alone or the current element plus max_current
        max_current = max(num, max_current + num)
        # Update max_global if the new max_current is greater
        max_global = max(max_global, max_current)

    return max_global


array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
result = max_sum_subarray(array)
print(f"The maximum sum of the subarray is: {result}")