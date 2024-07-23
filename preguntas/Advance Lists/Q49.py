# 49. Write a Python program to create a list of tuples 
# representing a histogram.

from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

frequency = Counter(data)
histogram = list(frequency.items())

print("Data:", data)
print("Histogram:", histogram)
