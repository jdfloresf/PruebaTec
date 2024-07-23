# 47. Write a Python program to concatenate two lists index-wise

list1 = ['a', 'b', 'c']
list2 = ['1', '2', '3']

if len(list1) != len(list2):
    raise ValueError("Lists must have the same length to concatenate index-wise.")
    
# Use zip to pair elements from both lists
concatenated_list = [str(a) + str(b) for a, b in zip(list1, list2)]
print("List 1:", list1)
print("List 2:", list2)
print("Concatenated list:", concatenated_list)
