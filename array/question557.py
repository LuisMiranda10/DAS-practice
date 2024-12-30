# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# Reverse Words in a String 3 


# Solution Using Two Pointer
class Solution:
    def reverseWords(self, s):
        pointer = 0
        answer = ""
        for index, char in enumerate(s):
            if char == " ":
                answer += s[pointer:index][::-1] + " "
                pointer = index + 1
            
        answer += s[pointer:len(s)][::-1]

        return answer

objeto = Solution()
print(objeto.reverseWords("Mr Ding"))