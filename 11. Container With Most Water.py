# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/17 下午7:50
# @Author  : zhanzecheng
# @File    : 11. Container With Most Water.py
# @Software: PyCharm
"""
'''
  y ^
    |
    |     a2
    |     |  a3          an
    |  a1 |  |     a5    | 
    |  |  |  |  a4 |     |
    |  |  |  |  |  | ..  |
    --------------------------->
   0   1  2  3  4  5 ..  n     x
'''

# 核心思路是一个二分查找的题， 小的进行移动，直到重叠

# TODO: check 1

# use the clamp
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        i, j = 0, length - 1
        water = 0
        while(i < j):
            water = max(water , min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -=1
        return water