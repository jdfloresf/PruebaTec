# 88. Write a Python program to find the sum of odd numbers in a list.


lst = [1, 2, 3, 4, 5, 10, 13, 17, 18, 20, 21, 25, 30, 43]

odd = [n for n in lst if n%2 == 1]

print(f"Even numbers: {odd}")
print(f"Sum of even numbers: {sum(odd)}")