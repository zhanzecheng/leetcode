# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/21 下午10:00
# @Author  : zhanzecheng
# @File    : 33. Search_in_rotated_sorted_array.py
# @Software: PyCharm
"""
import copy
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 下面这个用来找数组中的最小值
        low = 0
        hight = len(nums) - 1
        while low < hight:
            middle = (low + hight) // 2
            if(nums[middle] > nums[hight]):
                low = middle + 1
            else:
                hight = middle
        rot = low
        low = 0
        hight = len(nums) - 1
        tmp = copy.copy(nums)
        tmp[:(hight+1 -rot)] = nums[rot:]

        tmp[(hight+1-rot):] = nums[:rot]

        nums = tmp
        while low <= hight:
            middle = (low + hight) // 2
            if nums[middle] == target:
                middle += rot
                return middle % len(nums)
            elif nums[middle] < target:
                low = middle + 1
            elif nums[middle] > target:
                hight = middle - 1

        return -1

if __name__ == '__main__':
    data = [3, 5, 1]
    solution = Solution()
    print(solution.search(data, 3))