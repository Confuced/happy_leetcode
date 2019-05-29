# coding=utf-8
# 第266道题
# 答案来源
# https://www.cnblogs.com/grandyang/p/5223238.html
class Solution:
    def is_permute_palindrome(self, str1):
        if not str1:
            return False
        str_to_dict = {}
        for i in str1:
            if str_to_dict.get(i):
                str_to_dict[i] += 1
            else:
                str_to_dict[i] = 1
        # 如果是字符长度奇数，那么
        odd_count = 0
        for k, v in str_to_dict.items():
            if v % 2 == 1:
                odd_count += 1
        if len(str1)%2 == 1:
            if odd_count > 1:
                return False
        else:
            if odd_count > 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    test1 = 'code'
    test1 = 'aba'
    test1 = 'aab'
    test1 = 'carerac'
    test1 = ''
    test1 = 'a'
    result1 = s.is_permute_palindrome(test1)
    print(result1)