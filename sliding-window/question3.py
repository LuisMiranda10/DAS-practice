# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Longest Substring Without Repeating Characters

arr = "pwwkew"

left = 0
max_length = 0
hasher = {}

for right, i in enumerate(arr):
    hasher[i] = 1 + hasher.get(i, 0)
    while hasher[i] > 1:
        hasher[arr[left]] -= 1
        left += 1
        
    max_length = max(max_length, right - left + 1)

print(max_length)