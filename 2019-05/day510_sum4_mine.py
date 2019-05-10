# coding=utf-8
# 不看别人的，自己默写
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        #TODO
        # 这个算法有问题，等有空再写
        pass

    def nSum(self, nums, target, n, result, results):
        if n == 2:
            for i in range(0, len(nums)):
                l, r = 0, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        result = result + [nums[l], nums[r]]
                        results.append(result)
                        result = result[:-2]
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < target: l += 1
                    else:
                         r -= 1
        else:
            if n * nums[1] > target or n * nums[-1] < target: return
            else:
                for i in range(0, len(nums)):
                    if i == 0 or i > 0 and nums[i-1] != nums[i]:
                        self.nSum(nums[i+1:], target-nums[i], n-1, result+[nums[i]], results)



