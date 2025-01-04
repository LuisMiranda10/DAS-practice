# Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/
# First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hasher = {}
        for index, char in enumerate(s):
            if not hasher.get(char):
                hasher[char] = [index, 1]
            else:
                hasher[char][1] += 1
        
        for index, val in hasher.items():
            if val[1] == 1:
                return val[0]

        return -1