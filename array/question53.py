# Link: https://leetcode.com/problems/maximum-subarray/
# Maximum Subarray


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _maxSubArray, curr_sum = ("-inf"), 0 
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            _maxSubArray = max(_maxSubArray, curr_sum)
        return _maxSubArray