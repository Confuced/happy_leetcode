# coding=utf-8
# 2019-06-11 22:45:52
# url: https://leetcode.com/problems/valid-palindrome-ii/

# desc:
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution(object):
    def validPalindrome(self, s):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l+1, r) or self.isPalindrome(s, l, r-1)
            else:
                l += 1
                r -= 1
        return True


    def isPalindrome(self, s, l, r):
        while s[l] == s[r] and l < r:
            l += 1
            r -= 1
        if l >= r:
            return True
        return False




if __name__ == '__main__':
    s = Solution()
    case1 = 'abc'
    print(s.validPalindrome(case1))