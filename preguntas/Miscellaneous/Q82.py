# 82. Write a Python program to find the difference between two lists.

def list_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    only_in_list1 = list(set1 - set2)  # Elements in list1 but not in list2
    only_in_list2 = list(set2 - set1)  # Elements in list2 but not in list1
    
    return (only_in_list1, only_in_list2)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

diff1, diff2 = list_difference(list1, list2)
print(f"Elements in list1 but not in list2: {diff1}")
print(f"Elements in list2 but not in list1: {diff2}")
