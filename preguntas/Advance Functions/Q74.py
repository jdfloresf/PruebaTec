# 74. Write a Python function to implement insertion sort.

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


lista = [19,32,1,87,43,17]
print(f"Original array: {lista}")
insertion_sort(lista)
print(f"Sorted array: {lista}")