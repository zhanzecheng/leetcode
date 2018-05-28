# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 下午12:56
# @Author  : zhanzecheng
# @File    : 77. 数字组合.py
# @Software: PyCharm
"""


class Solution:
    def __init__(self):
        self.result = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        nums = [x for x in range(1, n + 1)]
        self._dfs(nums,[],k)
        return self.result
    def _dfs(self, nums, re, k):
        if k <= 0:
            if k == 0:
                self.result.append(re)
            return

        for i in range(len(nums)):
            re_ = re.copy()
            re_.append(nums[i])
            nums_ = nums.copy()
            nums_ = nums_[i+1:]
            self._dfs(nums_, re_, k - 1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))