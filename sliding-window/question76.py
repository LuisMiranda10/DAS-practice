# Link: https://leetcode.com/problems/minimum-window-substring/
# Minimum Window Substring

s = "ADOBECODEBANC"
t = "ABC"

left = 0
hasher = {}
minimum_window = float('inf')
splitado = list(t)

if len(s) < len(t):
    print("")    

for right, letter in enumerate(s):
    if letter in splitado and hasher.get(letter) is None:
        hasher[letter] = 1
        if len(t) == len(hasher):
            minimum_window = min(minimum_window, right - left + 1)
            del hasher[s[left]]
            left += 1

print(minimum_window)

# nao terminei