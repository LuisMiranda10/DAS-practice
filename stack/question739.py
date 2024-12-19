# 739. Daily temperatures - https://leetcode.com/problems/daily-temperatures/
# Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures):
        results = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]: 
                index = stack.pop()
                results[index] = i - index
            stack.append(i)
        
        return results