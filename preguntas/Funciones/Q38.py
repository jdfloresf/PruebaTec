# 38. Write a Python function to count the number of vowels in a string.

def vowels_count(string):
    count = 0 
    for vowel in string:
        if vowel in "aeiou":
            count += 1

    return count


string = "Hola como estais chavales"
print(f"Number of vowels: {vowels_count(string)}")

