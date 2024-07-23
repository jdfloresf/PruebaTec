# 93. Write a Python program to rotate a matrix 90 degrees clockwise.

def rotate_matrix_90_clockwise(matrix):
    """
    Rotate a matrix 90 degrees clockwise.

    Parameters:
    matrix (list of list of int): The matrix to rotate.

    Returns:
    list of list of int: The rotated matrix.
    """
    if not matrix or not matrix[0]:
        return matrix
    
    # Transpose the matrix
    transposed = list(zip(*matrix))
    
    # Reverse each row of the transposed matrix
    rotated = [list(row)[::-1] for row in transposed]
    
    return rotated


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_matrix_90_clockwise(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
    
print("\nRotated matrix 90 degrees clockwise:")
for row in rotated_matrix:
    print(row)
