# 43. Write a Python program to rotate the elements of a list.

def rotate_list(lst, positions):
    """Rotate the elements of a list to the right by a given number of positions."""
    if not lst:
        return lst  # Return empty list as is
    
    positions = positions % len(lst)  # Handle cases where positions > len(lst)
    return lst[-positions:] + lst[:-positions]


my_list = [1, 2, 3, 4, 5]
positions = 3
rotated_list = rotate_list(my_list, positions)
print("Original list:", my_list)
print(f"List rotated by {positions} positions to the right:", rotated_list)
