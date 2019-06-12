#coding=utf-8

# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
# Note:
#
# The input string length won't exceed 1000.

# coding=utf-8
# 2019-05-29 18:01:30

class Solution:
    def countSubstrings(self, s):
        res = [] # abbreviation of result
        for i in range(len(s)):
            # odd case
            self.helper(s, i, i, res)
            # even case
            self.helper(s, i, i + 1, res)
        return len(res)

    # the auxiliary function to pick out a palindrome
    def helper(self, s, l, r, res):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # it's very import and tricky to pass the result list in
            # because we have to record every palindrome
            res.append(s[l:r+1])
            l -= 1
            r += 1


if __name__ == '__main__':
    s = Solution()
    test1 = 'aaa'
    # test1 = 'abc'
    res = s.countSubstrings(test1)
    print(res)
