# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/13 下午7:07
# @Author  : zhanzecheng
# @File    : 633.easy_平方数的和.py
# @Software: PyCharm
"""
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range( int(c ** 0.5) + 1):
            j = c - i ** 2
            if int(j ** 0.5) ** 2 == j:
                return True
        return False