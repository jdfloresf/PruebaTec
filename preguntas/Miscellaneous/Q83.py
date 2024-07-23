# 83. Write a Python program to find the union of two lists

def list_union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    union_set = set1.union(set2)
    return list(union_set)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union_list = list_union(list1, list2)
print(f"Union of the two lists: {union_list}")
