# coding=utf-8
# 896. Monotonic Array
# Easy
# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.
#
#
#
# Example 1:
#
# Input: [1,2,2,3]
# Output: true
# Example 2:
#
# Input: [6,5,4,4]
# Output: true
# Example 3:
#
# Input: [1,3,2]
# Output: false
# Example 4:
#
# Input: [1,2,4,5]
# Output: true
# Example 5:
#
# Input: [1,1,1]
# Output: true
#
#
# Note:
#
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
List = list
class Solution:
    def isMonotonic(self, A):
        length = len(A)
        if length <= 2:
            return True
        asc, desc = True, True
        i = 1
        while i < length:
            asc = asc and True if A[i] >= A[i-1] else False
            desc = desc and True if A[i] <= A[i-1] else False
            i += 1
        return asc or desc

    def isMonotonic_todo(self, A) :
        length = len(A)
        if length <= 2:
            return True
        asc, desc = False, False
        if A[1] > A[0]:
            asc = True
        else:
            desc = True
        i = 2
        while True:
            pass


if __name__ == '__main__':
    s = Solution()
    test1 = [1,2,2,3]
    test1 = [4,2,2,3]
    res = s.isMonotonic(test1)
    print(res)