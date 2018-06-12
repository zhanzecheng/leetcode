# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 下午7:45
# @Author  : zhanzecheng
# @File    : 658.K个最接近的数.py
# @Software: PyCharm
"""

from bisect import *

# 先二分查找在左右指针

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        index = bisect_left(arr, x)

        left = index - 1
        right = index
        leftOutput = []
        rightOutput = []

        while right - (left + 1) < k:
            if left < 0:
                rightOutput.append(arr[right])
                right += 1
            elif right >= len(arr):
                leftOutput.append(arr[left])
                left -= 1
            elif abs(x - arr[left]) <= abs(x - arr[right]):
                leftOutput.append(arr[left])
                left -= 1
            else:
                rightOutput.append(arr[right])
                right += 1

        return leftOutput[::-1] + rightOutput