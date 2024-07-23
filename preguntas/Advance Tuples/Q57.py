# 57. Write a Python program to find the index of an item of a tuple in a 
# list of tuples.

list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
target_tuple = (1,2,3)

for i, tpl in enumerate(list_of_tuples):
    if tpl == target_tuple:
        index = i

if index != -1:
    print(f"The index of the tuple {target_tuple} is {index}.")
else:
    print(f"The tuple {target_tuple} is not found in the list.")
