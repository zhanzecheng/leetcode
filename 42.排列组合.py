# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/23 下午4:21
# @Author  : zhanzecheng
# @File    : 42.排列组合.py
# @Software: PyCharm
"""

class Solution:
    def __init__(self):
        self.result = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        for i in range(length):
            tmp = nums.copy()
            del tmp[i]
            now = []
            now.append(nums[i])
            self._DFS(tmp, now)
        return self.result

    def _DFS(self, nums, tmp):
        if len(nums) == 0:
            self.result.append(tmp)
            return
        length = len(nums)
        for i in range(length):
            dd = nums.copy()
            del dd[i]
            tmpp = tmp.copy()
            tmpp.append(nums[i])
            self._DFS(dd, tmpp)

if __name__ == '__main__':
    solution = Solution()
    data = [1, 1, 3]
    print(solution.permute(data))