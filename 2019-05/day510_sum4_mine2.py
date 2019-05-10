# coding=utf-8
# 不看别人的，自己默写
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result, results = [], []
        self.nSum(nums, target, 4, result, results)
        return results

    def _2sum(self, nums, target):
        result = []
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                result.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l-1] == nums[l]: l += 1
                while l < r and nums[r+1] == nums[l]: r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return result

    def nSum(self, nums, target, n, result, results):
        if n <= 2:
            tmp_result = self._2sum(nums, target)
            result = [result + item for item in tmp_result]
            results.extend(result)
        else:
            for i in range(0, len(nums)-n+1):
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.nSum(nums[i+1:], target-nums[i], n-1, result+[nums[i]], results)

# 经过艰苦的测试：
# 我得出教训：
# 函数分离有分离的好处， 也有分离的坏处。
# 另外，从2sum，到3sum，到4sum， 虽然看起来是简单的增加，但是代码扩展其实不是那么简单的。
# 在递归算法中，注意函数结束时参数的变化，
# 是永久的改变还是临时的改变，本次运行会不会对下次运行影响等等，这是编程语言的传参基本知识， 请加强掌握

# 函数分离会造成额外的负担， 切不利于算法内部的数据集成
# 函数之间的数据交换是有成本的， 所以在线OJ也尽量不要拆太多的方法，否则运行效率会降低。

if __name__ == '__main__':
    list1 = [3, 1, 1, 0, 2, 5, 6, 11, 9, 8]
    list1 = [1,0,-1,0,-2,2]
    target = 0
    s = Solution()
    print(s.fourSum(list1, target))