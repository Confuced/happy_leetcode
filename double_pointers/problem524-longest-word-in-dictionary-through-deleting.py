# coding=utf-8

# problem524-longest-word-in-dictionary-through-deleting
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/


# reference: https://www.cnblogs.com/grandyang/p/6523344.html

# 524. Longest Word in Dictionary through Deleting

# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
#
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.

class Solution(object):
    def findLongestWord(self, s, d):
        d.sort(key=len)  # TODO
        d.sort()
        longest = ''
        for v in d:
            i = j = 0
            while i < len(s) and j < len(v):
                if s[i] == v[j]:
                    j += 1
                i += 1
            if j == len(v):
                if len(v) > len(longest):
                    longest = v
                if len(v) == len(longest) and v < longest:
                    longest = v
        return longest
