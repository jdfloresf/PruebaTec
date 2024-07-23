# 54. Write a Python program to count the elements in a list until an element is a tuple.

lista = [1, 2.2, [1,2,3], "goa", (4, 5), True]
    
count = 0
for element in lista:
    if isinstance(element, tuple):
        break
    count += 1

print("Number of elements before the tuple:", count)
