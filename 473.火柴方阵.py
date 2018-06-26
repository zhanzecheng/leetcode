# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/25 下午12:01
# @Author  : zhanzecheng
# @File    : 473.火柴方阵.py
# @Software: PyCharm
"""

class Solution:
    def makesquare(self, nums_, k=4):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if sum(nums_) % k != 0:
            return False
        self.flag = False
        self.data = []
        target = sum(nums_) // k
        visit = [0] * len(nums_)

        def dfs(nums, visited, start_index, k, cur_sum):
            if k == 1:
                return True
            if cur_sum == target:
                return dfs(nums, visited, 0, k - 1, 0)
            if cur_sum > target:
                return False

            for i in range(start_index, len(nums)):
                if visited[i] == 0:
                    visited[i] = 1
                    if dfs(nums, visited, i + 1, k, cur_sum + nums[i]):
                        return True
                    visited[i] = 0
            return False

        return dfs(nums_, visit, 0, k, 0)

if __name__ == '__main__':
    solution = Solution()

    data =[2,2,10,5,2,7,2,2,13]


    k = 3
    print(solution.canPartitionKSubsets(data, k))