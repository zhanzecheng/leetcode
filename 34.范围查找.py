# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/4 上午10:43
# @Author  : zhanzecheng
# @File    : 34.范围查找.py
# @Software: PyCharm
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        length = len(nums)
        if length < 1:
            return [-1, -1]

        # now use binary search
        low = 0
        height = length - 1
        flag = False
        while low <= height:
            middle = (low + height) // 2
            if nums[middle] > target:
                height = middle - 1
            elif nums[middle] < target:
                low = middle + 1
            else:
                low = middle
                flag = True
                break
        if not flag:
            return [-1, -1]
        l = 0
        for i in range(low, -1, -1):
            if nums[i] != target:
                l = i + 1
                break
        h = length-1
        for i in range(low, length):
            if nums[i] != target:
                h = i - 1
                break
        return [l, h]
if __name__ == '__main__':
    solution = Solution()
    data = [1, 2, 3]
    print(solution.searchRange(data, target=2))