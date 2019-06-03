# coding=utf-8
# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".
class Solution:
    def reverseVowels(self, s: str) -> str:
        l, h = 0, len(s)-1
        vowels = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
        s_list = list(s)
        while l < h:
            if s[l] in vowels and s[h] in vowels:
                tmp = s_list[l]
                s_list[l] = s_list[h]
                s_list[h] = tmp
                l += 1
                h -= 1
            else:
                if s[l] not in vowels:
                    l += 1
                if s[h] not in vowels:
                    h -= 1
        return ''.join(s_list)

if __name__ == '__main__':
    s = Solution()
    test1 = 'hello'
    # test1 = 'leetcode'
    res = s.reverseVowels(test1)
    print(res)