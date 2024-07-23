# 81. Write a Python program to find the common elements in three lists.

def common_elements(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    common = set1.intersection(set2).intersection(set3)
    
    return list(common)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 8, 9, 10, 4]

print(f"Common elements: {common_elements(list1, list2, list3)}")
