# Link: https://leetcode.com/problems/binary-number-with-alternating-bits/description/
# Binary Number with Alternating Bits

nums = [5]
k = 1

left = 0
maximum_average = float('-inf')
soma = 0

for right, i in enumerate(nums):
    soma += i
    if (right - left + 1 == k):
        maximum_average = max(maximum_average, (soma/k))
        soma -= nums[left]
        left += 1

print(maximum_average)
        
# nao terminei