# coding=utf-8
# Given a string  s , you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
#
# Example 1:
#
# Input: "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
#
# Input: "abcd"
# Output: "dcbabcd"
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases. Thanks to @Freezen for additional test cases.

# 首先我们还是先将其的翻转字符串搞出来，然后比较原字符串s的前缀后翻转字符串t的对应位置的后缀是否相等，起始位置是比较s和t是否相等，
# 如果相等，说明s本身就是回文串，不用添加任何字符，直接返回即可；如果不想等，s去掉最后一位，t去掉第一位，继续比较，以此类推直至有相等，或者循环结束，这样我们就能将两个字符串在正确的位置拼接起来了，代码请参见评论区5楼。

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # get a reverse str
        s_reverse = s[::-1]
        sl, sr, srl, srr = 0, len(s), 0, len(s)
        while sl < sr:
            if s[sl:sr] != s_reverse[srl: srr]:
                sr = sr - 1
                srl = srl + 1
            else:
                break
        return s[sr:][::-1] + s


    def f1(self, s):
        return self.shortestPalindrome(s)

if __name__ == '__main__':
    s = Solution()
    test1 = 'abacdf'
    test1 = 'aacecaaa'
    test1 = 'abcd'
    # test1 = 'abad'
    result1 = s.f1(test1)
    print(result1)