# Link: https://leetcode.com/problems/longest-harmonious-subsequence/description/
# Longest Harmonious Subsequence

nums = [1,3,2,2,5,2,3,7]

left = 0
longest_subsequence = 0
hasher = {}

for number in nums:
    hasher[number] = 1 + hasher.get(number, 0)

for number in hasher:
    if number + 1 in hasher:
        longest_subsequence = max(longest_subsequence, hasher[number] + hasher[number + 1])
        
print(longest_subsequence)
    