# 95. Write a Python program to find the largest rectangle of 1's in a 
# binary matrix.

def max_histogram_area(heights):
    """
    Find the maximum area of a rectangle in a histogram.

    Parameters:
    heights (list of int): Heights of the histogram bars.

    Returns:
    int: The maximum area of the rectangle.
    """
    stack = []
    max_area = 0
    index = 0
    
    while index < len(heights):
        # Push the current bar to the stack if it is higher than the bar at the top of the stack
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Pop the top bar and calculate the area with heights[top] as the smallest (or minimum height) bar
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
    
    # Now pop the remaining bars from stack and calculate the area
    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
    
    return max_area

def max_rectangle_area(matrix):
    """
    Find the largest rectangle of 1's in a binary matrix.

    Parameters:
    matrix (list of list of int): The binary matrix.

    Returns:
    int: The area of the largest rectangle of 1's.
    """
    if not matrix or not matrix[0]:
        return 0
    
    max_area = 0
    heights = [0] * len(matrix[0])
    
    for row in matrix:
        # Update heights for each column
        for col in range(len(row)):
            heights[col] = heights[col] + 1 if row[col] == 1 else 0
        
        # Calculate the maximum area for the current histogram
        max_area = max(max_area, max_histogram_area(heights))
    
    return max_area


matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

area = max_rectangle_area(matrix)
print(f"Largest rectangle area of 1's: {area}")
