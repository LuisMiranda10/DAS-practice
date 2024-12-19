# Link: https://leetcode.com/problems/contains-duplicate-ii/description/
# Contains Duplicate II

from collections import defaultdict

nums = [1,2,3,1,1,2,3]
k = 0

left = 0
hasher = defaultdict(int)

for right, number in enumerate(nums):
    hasher[number] += 1
    if hasher[number] == 2:
        while nums[left] != nums[right]:
            left += 1
        if left is right:
            left -= 1
        if (abs(right - left) <= k):
            print(True)
        hasher[number] -= 1
        left += 1

print(False)