# coding=utf-8
# 今天的任务是找最长的回文子串
# problem5
# https://leetcode.com/problems/longest-palindromic-substring/
# 解法讲解参考 http://www.cnblogs.com/grandyang/p/4464476.html#commentform

class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        start, maxlen = 0, 0
        n = len(s)
        for i in range(0, n):
            start, maxlen = self.search_palindrome(s, i, i, start, maxlen)
            # 偶数次对称
            start, maxlen = self.search_palindrome(s, i, i+1, start, maxlen)
        return s[start:start+maxlen]



    def search_palindrome(self, s, left, right, start, maxlen):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 这里我需要解释一下代码， 为什么是 maxlen < right - left - 1 而不是 max < right - left + 1?
        # 明明长度是 right - left + 1嘛？
        # 原因是： 因为前面的那段代码里， left 多减了一次， right多加了一次， 所以要在这里 -1 调整回来
        if maxlen < right - left - 1:
            maxlen = right - left - 1
            start = left + 1
        return start, maxlen

if __name__ == '__main__':
    s = '"cbbd"'
    so = Solution()
    print(so.longestPalindrome(s))


