# 80. Write a Python function to find the longest common subsequence of 
# two strings.

import re
from itertools import combinations

def generate_subsequences(s):
    """Generate all subsequences of a string."""
    subsequences = []
    for i in range(len(s) + 1):
        for comb in combinations(s, i):
            subsequences.append(''.join(comb))
    return subsequences

def longest_common_subsequence_regex(s1, s2):
    """
    Find the longest common subsequence of two strings using regex.
    
    Parameters:
    s1 (str): The first string.
    s2 (str): The second string.
    
    Returns:
    str: The longest common subsequence.
    """
    subsequences = generate_subsequences(s1)
    longest_subseq = ""
    
    for subseq in subsequences:
        # Create a regex pattern to find the subsequence in s2
        pattern = '.*' + '.*'.join(subseq) + '.*'
        if re.fullmatch(pattern, s2):
            if len(subseq) > len(longest_subseq):
                longest_subseq = subseq
    
    return longest_subseq


s1 = "ABCBDAB"
s2 = "BDCAB"

print(f"Longest Common Subsequence: {longest_common_subsequence_regex(s1, s2)}")
