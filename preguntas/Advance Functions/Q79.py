# 79. Write a Python function to solve the knapsack problem using 
# dynamic programming.

def knapsack(values, weights, capacity):
    """
    Solve the knapsack problem using dynamic programming.

    Parameters:
    values (list): A list of values of the items.
    weights (list): A list of weights of the items.
    capacity (int): The maximum weight capacity of the knapsack.

    Returns:
    int: The maximum value that can be obtained without exceeding the capacity.
    """
    n = len(values)
    # Create a 2D array to store the maximum value that can be obtained
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # If including the current item is better than excluding it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # If the current item cannot be included
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(f"Maximum value that can be obtained: {knapsack(values, weights, capacity)}")
