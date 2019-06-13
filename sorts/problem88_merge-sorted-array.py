# coding=utf-8

# 88. Merge Sorted Array
# Easy
#
# 1097
#
# 2789
#
# Favorite
#
# Share
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index = 0
        while n > index:
            j = k = m + index - 1
            while nums2[index] < nums1[j] and j > -1:
                j -= 1
            while k-j > 0:# TODO
                nums1[k+1] = nums1[k]
                k -= 1
            nums1[k+1] = nums2[index]
            index += 1


if __name__ == '__main__':
    nums1 = [0,0,3,0,0,0,0,0,0]
    m = 3
    nums2 = [-1,1,1,1,2,3]
    n = 6
    s = Solution()
    s.merge(nums1, 3, nums2, 6)
    print(nums1)

