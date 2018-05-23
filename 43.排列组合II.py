# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/23 下午4:32
# @Author  : zhanzecheng
# @File    : 43.排列组合II.py
# @Software: PyCharm
"""


class Solution:
    def __init__(self):
        self.result = []
    def permuteUnique(self, nums):
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
            if tmp not in self.result:
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