"""
Smallest window that contains all characters of string itself
"""

from collections import defaultdict

string = "aabcbcdbca"

left = 0
smallest = float('inf')
distinct_letters = len(set(letter for letter in string))
hasher = defaultdict(int)
count = 0

for right, letter in enumerate(string):
    hasher[letter] += 1

    if hasher[letter] == 1:
        count += 1

    if count == distinct_letters:
        while hasher[string[left]] > 1:
            hasher[string[left]] -= 1
            left += 1
    
        if right - left + 1 < smallest:
            smallest = right - left + 1
            smallest_substring = string[left:right + 1]

print(smallest_substring)