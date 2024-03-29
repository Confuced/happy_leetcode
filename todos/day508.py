class Solution:

    def helper(self, s , start, out, res):
        length = len(s)

        if start == length:
            res.append(out)
            return
        for i in range(start, length):
            if not self.is_palindrome(s, start, i):
                continue
            out.append(s[start: i])
            self.helper(s, i+1, out, res)
            out.pop()

    def partition(self, s):
        res = []
        out = []
        self.helper(s, 0, out, res)
        return res


if __name__ == '__main__':
    str1 = 'aabc'
    s = Solution()
    output = s.partition(str1)
    print(output)