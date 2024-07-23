# 76. Write a Python function to implement heap sort.

def heapify(arr, n, i):
    """
    Convert a subtree rooted at index i into a max heap.
    
    Parameters:
    arr (list): The list to heapify.
    n (int): The size of the heap.
    i (int): The index of the root element of the subtree.
    """
    largest = i        # Initialize largest as root
    l = 2 * i + 1      # Left child index
    r = 2 * i + 2      # Right child index

    # Check if left child exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Check if right child exists and is greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Swap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heap_sort(arr):
    """
    Perform heap sort on a list.

    Parameters:
    arr (list): The list of elements to sort.

    Returns:
    list: The sorted list.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr


arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)
