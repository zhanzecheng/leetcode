# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 下午8:34
# @Author  : zhanzecheng
# @File    : 416.分为相等的和.py
# @Software: PyCharm
"""

# 又是一个背包问题
# 这是一个选或者不选的问题， 我们可以使用背包的思想， true false的思想来解决它

# TODO: check 1
class Solution:
    def canPartitionKSubsets(self, nums_, k=2):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if sum(nums_) % 2 != 0:
            return False
        target = sum(nums_) // 2
        dp = [[False] * (target+1) for _ in range(len(nums_)+1)]
        for i in range(len(nums_) + 1):
            dp[i][0] = True

        for i in range(1, len(nums_) + 1):
            for j in range(1, target + 1):
                if j >= nums_[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums_[i-1]]

        return dp[len(nums_)][target]

if __name__ == '__main__':
    solution = Solution()

    # data =[28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79]
    data = [1, 5, 11, 5]
    # data = [100,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(solution.canPartitionKSubsets(data))