# 42. Write a Python program to split a list into evenly sized chunks.

def chunk_list(lst, chunk_size):
    """Split a list into evenly sized chunks."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer")
 
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


my_list = [x for x in range(1, 21)]
chunk_size = 5
chunks = chunk_list(my_list, chunk_size)
print("Original list:", my_list)
print(f"List split into chunks of size {chunk_size}:", chunks)
