# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/13 下午5:17
# @Author  : zhanzecheng
# @File    : 605.摆花瓶.py
# @Software: PyCharm
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 1
        re = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                count += 1
            else:
                re += (count - 1) // 2
                count = 0
        if count != 0:
            re += (count ) // 2
        return re >= n