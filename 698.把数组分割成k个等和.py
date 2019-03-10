# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 下午5:26
# @Author  : zhanzecheng
# @File    : 698.把数组分割成k个等和.py
# @Software: PyCharm
"""

# 这个里面其实是包含了两个dfs

# TODO: check 1

# 这一题还是贼牛逼
class Solution:
    def canPartitionKSubsets(self, nums_, k):
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