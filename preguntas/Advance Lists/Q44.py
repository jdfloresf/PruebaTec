# 44. Write a Python program to find the cumulative sum of a list

def cumulative_sum(lst):
    """Calculate the cumulative sum of a list."""
    cum_sum = []
    total = 0
    for num in lst:
        total += num
        cum_sum.append(total)
    return cum_sum


numbers = [1, 2, 3, 4, 5]
result = cumulative_sum(numbers)
print("Original list:", numbers)
print("Cumulative sum:", result)
