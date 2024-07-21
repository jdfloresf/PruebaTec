#5. Write a Python program to find the second largest element in a list.

lista = [12,41,7,2,4,102,4124,34,1]

largest = s_largest = 0
for n in lista:
    if n > largest:
        s_largest = largest
        largest = n
    elif n > s_largest and n != largest:
        s_largest = n

print(f"lagest: {largest}")
print(f"Second largest: {s_largest}")
