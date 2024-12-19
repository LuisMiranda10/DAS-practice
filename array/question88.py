# Link: https://leetcode.com/problems/merge-sorted-array/description/
# Merge Sorted Array

class Solution:
    def merge(self, nums1, m: int, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len_nums1 = m -1 # tamanho de nums1 (somente a parte onde não contem os '0s')
        len_nums2 = n -1 # tamanho de nums2
        k = m + n - 1 # tamanho total de nums1
        
        while len_nums2 >= 0:
            if len_nums1 >= 0 and nums1[len_nums1] > nums2[len_nums2]:
                nums1[k] = nums1[len_nums1]
                len_nums1 -= 1
            else:
                nums1[k] = nums2[len_nums2]
                len_nums2 -= 1
            k -=1