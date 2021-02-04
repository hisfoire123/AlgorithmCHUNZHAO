# 283 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
class Solution:
    def moveZeroes(self, nums: list) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] , nums[i]= nums[i] , nums[j]
                j += 1


class Solution:
    def moveZeroes(self, nums: list) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1
        return nums

# 70. 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2: return n
        a, b, temp = 1, 2, 0
        for i in range(3,n+1):
            temp = a + b
            a = b
            b = temp
        return temp

# 11. 盛最多水的容器
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

class Solution:
    def maxArea(self, height: list) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

# 1. 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
class Solution(object):
    def twoSum(self,nums: list, target:int) -> list:
        d = dict()
        for i, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], i]
            d[num] = i

# 15. 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res