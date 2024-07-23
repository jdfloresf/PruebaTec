# 41. Write a Python program to flatten a nested list.

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursively flatten the list
        else:
            flat_list.append(item)  # Add non-list items to the flat list
    return flat_list

# Example usage
if __name__ == "__main__":
    nested_list = [1, [2, [3, 4, [5, 6]], 7], 8, [9]]
    print("Original nested list:", nested_list)
    flattened = flatten(nested_list)
    print("Flattened list:", flattened)
