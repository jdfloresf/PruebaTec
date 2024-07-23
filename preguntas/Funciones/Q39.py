# 39. Write a Python function to check if a string is a palindrome.

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Remove punctuation
    s = ''.join(c for c in s if c.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]


str1 = "A man, a plan, a canal, Panama!"
str2 = "Not a palindrome"
    
print(f"'{str1}' is a palindrome: {is_palindrome(str1)}")
print(f"'{str2}' is a palindrome: {is_palindrome(str2)}")
