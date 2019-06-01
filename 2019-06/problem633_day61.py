# coding=utf-8
# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
#
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
#
#
# Example 2:
#
# Input: 3
# Output: False
#
#
# 这道题让我们求一个数是否能由平方数之和组成，刚开始博主没仔细看题，没有看到必须要是两个平方数之和，博主以为任意一个就可以。所以写了个带优化的递归解法，博主已经不是上来就无脑暴力破解的辣个青葱骚年了，直接带优化。可是居然对 14 返回 false，难道 14 不等于 1+4+9 吗，结果仔细一看，必须要两个平方数之和。好吧，那么递归都省了，直接判断两次就行了。我们可以从c的平方根，注意即使c不是平方数，也会返回一个整型数。然后我们判断如果 ii 等于c，说明c就是个平方数，只要再凑个0，就是两个平方数之和，返回 true；如果不等于的话，那么算出差值 c - ii，如果这个差值也是平方数的话，返回 true。遍历结束后返回 false，参见代码如下：

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math as m
        c_root = int(m.sqrt(c))
        while True:
            d = c - c_root*c_root
            d_root = int(m.sqrt(d))
            if d_root*d_root == d:
                print(c_root, d_root)
                return True
            else:
                c_root -= 1
                if c_root < d_root:
                    print(c_root, d_root)
                    return False


    # a large number 999999999 will cause timeout.
    def judgeSquareSum_fail(self, c: int) -> bool:
        import math as m
        c_root = int(m.sqrt(c))
        i = 0
        while i*i + c_root*c_root != c and i <= c_root:
            if i*i + c_root*c_root < c:
                i +=1
            elif i*i + c_root*c_root > c:
                c_root -= 1
                i = 0
        print(i, c_root)
        if i*i + c_root*c_root != c: return False
        return True



    def judgeSquareSum2(self, c: int) -> bool:
        import math as m
        c_root = int(m.sqrt(c))
        i = 0
        while i*i + c_root*c_root != c and i <= c_root:
            if i*i + c_root*c_root < c:
                i +=1
            elif i*i + c_root*c_root > c:
                c_root -= 1
                # i = 0
        print(i, c_root)
        if i*i + c_root*c_root != c: return False
        return True




if __name__ == '__main__':
    s = Solution()
    test1 = 10
    test1 = 5
    test1 = 72
    test1 = 1000
    test1 = 3
    test1 = 999999999
    res = s.judgeSquareSum2(test1)
    print(res)

# Time Submitted
# Status
# Runtime
# Memory
# Language
# 4 minutes ago	Accepted	168 ms	13.2 MB	python3
# 20 minutes ago	Time Limit Exceeded	N/A	N/A	python3
# 21 minutes ago	Wrong Answer	N/A	N/A	python3
# 32 minutes ago	Wrong Answer	N/A	N/A	python3