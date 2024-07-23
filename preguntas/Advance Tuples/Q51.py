# 51. Write a Python program to find the length of the longest tuple.

tuples_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10,)]
max_length = max(len(tpl) for tpl in tuples_list)

print("Length of the longest tuple:", max_length)
