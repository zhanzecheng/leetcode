# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 下午7:49
# @Author  : zhanzecheng
# @File    : 81.在旋转列表中招数.py
# @Software: PyCharm
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        for i in nums:
            if i == target:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()

    data = [2,2,2,0,2,2]
    print(solution.search(data, 2))