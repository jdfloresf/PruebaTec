# 92. Write a Python program to find the longest increasing subsequence
#  in a list.


lst = [10, 22, 9, 33, 21, 50, 41, 60, 80]

n = len(lst)
# dp[i] will be the length of the longest increasing subsequence ending at index i
dp = [1] * n
# Array to reconstruct the LIS
predecessor = [-1] * n
# Fill dp and predecessor arrays
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            predecessor[i] = j
# Find the index of the maximum value in dp array
max_index = dp.index(max(dp))
lis = []
while max_index != -1:
    lis.append(lst[max_index])
    max_index = predecessor[max_index]

lis[::-1]
print(f"Longest increasing subsequence: {lis}")