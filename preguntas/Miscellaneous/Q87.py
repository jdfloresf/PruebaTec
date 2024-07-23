# 87. Write a Python program to find the sum of even numbers in a list.

lst = [1, 2, 3, 4, 5, 10, 13, 17, 18, 20, 21, 25, 30, 43]

even = [n for n in lst if n%2 == 0]

print(f"Even numbers: {even}")
print(f"Sum of even numbers: {sum(even)}")